"""Test ``cosmology_api.api.core``."""

from __future__ import annotations

# STDLIB
from dataclasses import field, make_dataclass

# THIRD-PARTY
import numpy.array_api as xp

# LOCAL
from cosmology.api import FLRWCosmologyAPI
from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_flrw():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPI`.
    """
    # Simple example: missing everything

    class FLRW:
        pass

    cosmo = FLRW()

    assert not isinstance(cosmo, FLRWCosmologyAPI)

    # TODO: more examples?


def test_compliant_flrw(cosmology_cls, flrw_attrs, flrw_meths):
    """
    Test that an instance is `cosmology.api.FLRWCosmologyAPI` even if it
    doesn't inherit from `cosmology.api.FLRWCosmologyAPI`.
    """

    def _default_one() -> Array:
        return xp.ones((), dtype=xp.int32)

    def _return_one(self, /) -> Array:
        return _default_one()

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    fields = ("H0", "Om0", "Ode0", "Tcmb0", "Neff", "m_nu", "Ob0")

    FLRW = make_dataclass(
        "FLRW",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in flrw_attrs - set(fields)}
        | {n: _return_1arg for n in flrw_meths},
        frozen=True,
    )

    cosmo = FLRW()

    assert isinstance(cosmo, FLRWCosmologyAPI)


def test_fixture(flrw):
    """
    Test that the ``flrw`` fixture is a
    `cosmology.api.FLRWCosmologyAPI`.
    """
    assert isinstance(flrw, FLRWCosmologyAPI)
