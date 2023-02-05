"""Test ``cosmology.api.compat``."""

from __future__ import annotations

from dataclasses import dataclass

import pytest
from cosmology.api import (
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyWrapperAPI,
)

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyWrapperAPI`.
    """

    # Simple example: missing everything
    class ExampleCosmologyWrapper:
        pass

    wrapper = ExampleCosmologyWrapper()

    assert not isinstance(wrapper, CosmologyWrapperAPI)

    # TODO: more examples?


def test_compliant_cosmology(cosmology_ns):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyWrapperAPI`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    @dataclass
    class ExampleCosmologyWrapper:
        cosmo: object

        def __cosmology_namespace__(
            self,
            /,
            *,
            api_version: str | None = None,
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

        def __getattr__(self, name: str) -> object:
            return getattr(self.cosmo, name)

    wrapper = ExampleCosmologyWrapper(object())

    assert isinstance(wrapper, CosmologyAPI)
    assert isinstance(wrapper, CosmologyWrapperAPI)


class Test_CosmologyWrapperAPI:
    @pytest.fixture(scope="class")
    def wrapper_cls(
        self,
        cosmology_ns: CosmologyAPINamespace,
    ) -> type[CosmologyWrapperAPI]:
        @dataclass(frozen=True)
        class ExampleCosmologyWrapper(CosmologyWrapperAPI):
            cosmo: object

            def __cosmology_namespace__(
                self,
                /,
                *,
                api_version: str | None = None,
            ) -> CosmologyAPINamespace:
                return cosmology_ns

            @property
            def name(self) -> str | None:
                return None

        return ExampleCosmologyWrapper

    @pytest.fixture(scope="class")
    def wrapper(
        self,
        cosmology: object,
        wrapper_cls: type[CosmologyWrapperAPI],
    ) -> CosmologyWrapperAPI:
        return wrapper_cls(cosmology)

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, CosmologyAPI)
        assert isinstance(wrapper, CosmologyWrapperAPI)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute
