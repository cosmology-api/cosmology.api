"""Test ``cosmology_api.api.core``."""

from __future__ import annotations

# STDLIB
from dataclasses import field, make_dataclass

# THIRD-PARTY
import numpy.array_api as xp

# LOCAL
from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_bkg():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPI`.
    """
    # Simple example: missing everything

    class StandardCosmology:
        pass

    cosmo = StandardCosmology()

    assert not isinstance(cosmo, StandardCosmologyAPI)

    # TODO: more examples?


def test_compliant_bkg(cosmology_cls, standard_attrs, standard_meths):
    """
    Test that an instance is `cosmology.api.StandardCosmologyAPI` even if it
    doesn't inherit from `cosmology.api.StandardCosmologyAPI`.
    """

    def _default_one() -> Array:
        return xp.ones((), dtype=xp.int32)

    def _return_one(self, /) -> Array:
        return _default_one()

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    fields = ("H0", "Om0", "Ode0", "Tcmb0", "Neff", "m_nu", "Ob0")

    StandardCosmology = make_dataclass(
        "StandardCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in standard_attrs - set(fields)}
        | {n: _return_1arg for n in standard_meths},
        frozen=True,
    )

    cosmo = StandardCosmology()

    assert isinstance(cosmo, StandardCosmologyAPI)


def test_fixture(standardcosmo):
    """
    Test that the ``standardcosmo`` fixture is a
    `cosmology.api.StandardCosmologyAPI`.
    """
    assert isinstance(standardcosmo, StandardCosmologyAPI)
