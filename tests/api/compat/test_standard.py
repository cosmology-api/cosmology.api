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
    StandardCosmologyAPI,
    StandardCosmologyWrapperAPI,
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
    class StandardCosmologyWrapper:
        pass

    wrapper = StandardCosmologyWrapper()

    assert not isinstance(wrapper, StandardCosmologyWrapperAPI)

    # TODO: more examples?


def test_compliant_bkg_wrapper(cosmology_ns, standard_attrs, standard_meths):
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

    StandardCosmologyWrapper = make_dataclass(
        "StandardCosmologyWrapper",
        [("cosmo", object)],
        namespace={n: property(_return_one) for n in standard_attrs}
        | {n: _return_1arg for n in standard_meths}
        | {
            "__cosmology_namespace__": _cosmology_namespace_,
            "name": property(name),
            "__getattr__": _getattr_,
        },
        frozen=True,
    )

    wrapper = StandardCosmologyWrapper(object())

    assert isinstance(wrapper, CosmologyAPI)
    assert isinstance(wrapper, CosmologyWrapperAPI)
    assert isinstance(wrapper, BackgroundCosmologyAPI)
    assert isinstance(wrapper, BackgroundCosmologyWrapperAPI)
    assert isinstance(wrapper, StandardCosmologyAPI)
    assert isinstance(wrapper, StandardCosmologyWrapperAPI)


class Test_CosmologyWrapperAPI:
    @pytest.fixture(scope="class")
    def wrapper_cls(
        self,
        cosmology_ns: CosmologyAPINamespace,
    ) -> type[StandardCosmologyWrapperAPI]:
        @dataclass(frozen=True)
        class StandardCosmologyWrapper(StandardCosmologyWrapperAPI):

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

        return StandardCosmologyWrapper

    @pytest.fixture(scope="class")
    def wrapper(
        self,
        wrapper_cls: type[StandardCosmologyWrapperAPI],
    ) -> StandardCosmologyWrapperAPI:
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
