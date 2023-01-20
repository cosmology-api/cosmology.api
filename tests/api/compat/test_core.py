"""Test ``cosmology_api.api.compat``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass

import pytest

# LOCAL
from cosmology.api import (
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyWrapper,
)

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyWrapper`.
    """
    # Simple example: missing everything
    class CosmologyWrapper:
        pass

    wrapper = CosmologyWrapper()

    assert not isinstance(wrapper, CosmologyWrapper)

    # TODO: more examples?


def test_compliant_cosmology(cosmology_ns):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyWrapper`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    @dataclass
    class CosmologyWrapper:

        cosmo: object

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

        def __getattr__(self, name: str) -> object:
            return getattr(self.cosmo, name)

    wrapper = CosmologyWrapper(object())

    assert isinstance(wrapper, CosmologyAPI)
    assert isinstance(wrapper, CosmologyWrapper)


class Test_CosmologyWrapper:
    @pytest.fixture(scope="class")
    def wrapper_cls(
        self, cosmology_ns: CosmologyAPINamespace
    ) -> type[CosmologyWrapper]:
        @dataclass(frozen=True)
        class CosmologyWrapper(CosmologyWrapper):

            cosmo: object

            def __cosmology_namespace__(
                self, /, *, api_version: str | None = None
            ) -> CosmologyAPINamespace:
                return cosmology_ns

            @property
            def name(self) -> str | None:
                return None

        return CosmologyWrapper

    @pytest.fixture(scope="class")
    def wrapper(
        self, cosmology: object, wrapper_cls: type[CosmologyWrapper]
    ) -> CosmologyWrapper:
        return wrapper_cls(cosmology)

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, CosmologyAPI)
        assert isinstance(wrapper, CosmologyWrapper)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute
