"""Test ``cosmology_api.api.compat``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass, make_dataclass

# THIRD-PARTY
import numpy.array_api as xp
import pytest

# LOCAL
from cosmology.api import (
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyWrapper,
    FLRWCosmologyAPI,
    FLRWCosmologyWrapper,
)
from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.FLRWCosmologyWrapper`.
    """
    # Simple example: missing everything
    class FLRWWrapper:
        pass

    wrapper = FLRWWrapper()

    assert not isinstance(wrapper, CosmologyWrapper)

    # TODO: more examples?


def test_compliant_flrw_wrapper(cosmology_ns, flrw_attrs, flrw_meths):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyWrapper`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    def _return_one(self, /) -> Array:
        return xp.ones((), dtype=xp.int32)

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    def _cosmology_namespace_(
        self, /, *, api_version: str | None = None
    ) -> CosmologyAPINamespace:
        return cosmology_ns

    def name(self) -> str | None:
        return None

    def _getattr_(self, name: str) -> object:
        return getattr(self.cosmo, name)

    FLRWWrapper = make_dataclass(
        "FLRWWrapper",
        [("cosmo", object)],
        namespace={n: property(_return_one) for n in flrw_attrs}
        | {n: _return_1arg for n in flrw_meths}
        | {
            "__cosmology_namespace__": _cosmology_namespace_,
            "name": property(name),
            "__getattr__": _getattr_,
        },
        frozen=True,
    )

    wrapper = FLRWWrapper(object())

    assert isinstance(wrapper, CosmologyAPI)
    assert isinstance(wrapper, CosmologyWrapper)
    assert isinstance(wrapper, FLRWCosmologyAPI)
    assert isinstance(wrapper, FLRWCosmologyWrapper)


class Test_CosmologyWrapper:
    @pytest.fixture(scope="class")
    def wrapper_cls(self, cosmology_ns):
        @dataclass(frozen=True)
        class FLRWWrapper(FLRWCosmologyWrapper):

            cosmo: object

            def __cosmology_namespace__(
                self, /, *, api_version: str | None = None
            ) -> CosmologyAPINamespace:
                return cosmology_ns

            @property
            def name(self) -> str | None:
                return None

            # === Not Cosmology API ===

            @property
            def not_cosmology_api(self) -> int:
                return 1

        return FLRWWrapper

    @pytest.fixture(scope="class")
    def wrapper(self, wrapper_cls):
        return wrapper_cls(object())

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, CosmologyAPI)
        assert isinstance(wrapper, CosmologyWrapper)
        assert isinstance(wrapper, FLRWCosmologyAPI)
        assert isinstance(wrapper, FLRWCosmologyWrapper)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute
