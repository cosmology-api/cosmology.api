"""Test ``cosmology_api.api.compat``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass, make_dataclass
from typing import TYPE_CHECKING

# THIRD-PARTY
import numpy.array_api as xp
import pytest

# LOCAL
from cosmology.api import (
    BackgroundCosmologyAPI,
    BackgroundCosmologyWrapperAPI,
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyWrapperAPI,
)

if TYPE_CHECKING:
    from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.BackgroundCosmologyWrapperAPI`.
    """
    # Simple example: missing everything
    class BackgroundWrapper:
        pass

    wrapper = BackgroundWrapper()

    assert not isinstance(wrapper, BackgroundCosmologyWrapperAPI)

    # TODO: more examples?


def test_compliant_bkg_wrapper(cosmology_ns, background_attrs, background_meths):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyWrapperAPI`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    def _return_one(self, /) -> Array:
        return xp.ones((), dtype=xp.int32)

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    def _cosmology_namespace_(
        self,
        /,
        *,
        api_version: str | None = None,
    ) -> CosmologyAPINamespace:
        return cosmology_ns

    def name(self) -> str | None:
        return None

    def _getattr_(self, name: str) -> object:
        return getattr(self.cosmo, name)

    BackgroundWrapper = make_dataclass(
        "BackgroundWrapper",
        [("cosmo", object)],
        namespace={n: property(_return_one) for n in background_attrs}
        | {n: _return_1arg for n in background_meths}
        | {
            "__cosmology_namespace__": _cosmology_namespace_,
            "name": property(name),
            "__getattr__": _getattr_,
        },
        frozen=True,
    )

    wrapper = BackgroundWrapper(object())

    assert isinstance(wrapper, CosmologyAPI)
    assert isinstance(wrapper, CosmologyWrapperAPI)
    assert isinstance(wrapper, BackgroundCosmologyAPI)
    assert isinstance(wrapper, BackgroundCosmologyWrapperAPI)


class Test_BackgroundCosmologyWrapperAPI:
    @pytest.fixture(scope="class")
    def wrapper_cls(
        self,
        cosmology_ns: CosmologyAPINamespace,
    ) -> type[BackgroundCosmologyWrapperAPI]:
        @dataclass(frozen=True)
        class BackgroundWrapper(BackgroundCosmologyWrapperAPI):

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

            # === Not Cosmology API ===

            @property
            def not_cosmology_api(self) -> int:
                return 1

        return BackgroundWrapper

    @pytest.fixture(scope="class")
    def wrapper(
        self,
        wrapper_cls: type[BackgroundCosmologyWrapperAPI],
    ) -> BackgroundCosmologyWrapperAPI:
        return wrapper_cls(object())

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, CosmologyAPI)
        assert isinstance(wrapper, CosmologyWrapperAPI)
        assert isinstance(wrapper, BackgroundCosmologyAPI)
        assert isinstance(wrapper, BackgroundCosmologyWrapperAPI)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute
