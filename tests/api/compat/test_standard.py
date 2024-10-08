"""Test ``cosmology.api.compat``."""

from __future__ import annotations

from dataclasses import dataclass, make_dataclass
from importlib.metadata import version as get_version
from typing import TYPE_CHECKING

import pytest
from packaging.version import Version

from cosmology.api import (
    Cosmology,
    CosmologyConstantsNamespace,
    CosmologyNamespace,
    CosmologyWrapper,
    StandardCosmology,
    StandardCosmologyWrapper,
)

np_ve = Version(get_version("numpy"))
if np_ve >= Version("1.23") and np_ve < Version("2.1"):
    import numpy.array_api as np  # pragma: no cover
else:
    import numpy as np

if TYPE_CHECKING:
    from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.StandardCosmologyWrapper`.
    """

    # Simple example: missing everything
    class ExampleStandardCosmologyWrapper:
        pass

    wrapper = ExampleStandardCosmologyWrapper()

    assert not isinstance(wrapper, StandardCosmologyWrapper)

    # TODO: more examples?


def test_compliant_standard_wrapper(cosmology_ns, standard_attrs, standard_meths):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyWrapper`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    def _return_one(self, /) -> Array:
        return np.ones((), dtype=np.int32)

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    def _cosmology_namespace_(self) -> CosmologyNamespace:
        return cosmology_ns

    def name(self) -> str | None:
        return None

    def _getattr_(self, name: str) -> object:
        return getattr(self.cosmo, name)

    def constants(self) -> CosmologyConstantsNamespace:
        return cosmology_ns.constants

    ExampleStandardCosmologyWrapper = make_dataclass(
        "ExampleStandardCosmologyWrapper",
        [("cosmo", object)],
        namespace={n: property(_return_one) for n in standard_attrs}
        | {n: _return_1arg for n in standard_meths}
        | {
            "__cosmology_namespace__": property(_cosmology_namespace_),
            "name": property(name),
            "__getattr__": _getattr_,
            "constants": constants,
        },
        frozen=True,
    )

    wrapper = ExampleStandardCosmologyWrapper(object())

    assert isinstance(wrapper, Cosmology)
    assert isinstance(wrapper, CosmologyWrapper)
    assert isinstance(wrapper, StandardCosmology)
    assert isinstance(wrapper, StandardCosmologyWrapper)


class Test_StandardCosmologyWrapper:
    @pytest.fixture(scope="class")
    def wrapper_cls(
        self,
        cosmology_ns: CosmologyNamespace,
    ) -> type[StandardCosmologyWrapper]:
        @dataclass(frozen=True)
        class ExampleStandardCosmologyWrapper(StandardCosmologyWrapper):
            cosmo: object

            @property
            def __cosmology_namespace__(self) -> CosmologyNamespace:
                return cosmology_ns

            @property
            def name(self) -> str | None:
                return None

            # === Not Cosmology API ===

            @property
            def not_cosmology_api(self) -> int:
                return 1

        return ExampleStandardCosmologyWrapper

    @pytest.fixture(scope="class")
    def wrapper(
        self,
        wrapper_cls: type[StandardCosmologyWrapper],
    ) -> StandardCosmologyWrapper:
        return wrapper_cls(object())

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, Cosmology)
        assert isinstance(wrapper, CosmologyWrapper)
        assert isinstance(wrapper, StandardCosmologyWrapper)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute  # noqa: B018
