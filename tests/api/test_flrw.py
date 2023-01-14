"""Test ``cosmology_api.api.core``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass

# THIRD-PARTY
import numpy.array_api as xp

# LOCAL
from cosmology.api import CosmologyAPIConformant, FLRWAPIConformant
from cosmology.api._array_api.array import ArrayAPIConformant as Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_flrw():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPIConformant`.
    """
    # Simple example: missing everything

    class FLRW:
        pass

    cosmo = FLRW()

    assert not isinstance(cosmo, FLRWAPIConformant)

    # TODO: more examples?


def test_compliant_flrw(cosmology_cls: type[CosmologyAPIConformant]):
    """
    Test that an instance is `cosmology.api.FLRWAPIConformant` even if it
    doesn't inherit from `cosmology.api.FLRWAPIConformant`.
    """

    def return_one(self, /) -> Array:
        return xp.ones((), dtype=xp.int32)

    def return_1arg(self, z: Array, /) -> Array:
        return z

    @dataclass(frozen=True)
    class FLRW(cosmology_cls):
        H0: Array = xp.ones((), dtype=xp.int32)
        Om0: Array = xp.ones((), dtype=xp.int32)
        Ode0: Array = xp.ones((), dtype=xp.int32)
        Tcmb0: Array = xp.ones((), dtype=xp.int32)
        Neff: Array = xp.ones((), dtype=xp.int32)
        m_nu: Array = xp.ones((), dtype=xp.int32)
        Ob0: Array = xp.ones((), dtype=xp.int32)
        name: str | None = None

        scale_factor0 = property(return_one)
        h = property(return_one)
        hubble_distance = property(return_one)
        hubble_time = property(return_one)
        Otot0 = property(return_one)
        Odm0 = property(return_one)
        Ok0 = property(return_one)
        Ogamma0 = property(return_one)
        Onu0 = property(return_one)

        rho_critical0 = property(return_one)
        rho_tot0 = property(return_one)
        rho_m0 = property(return_one)
        rho_de0 = property(return_one)
        rho_b0 = property(return_one)
        rho_dm0 = property(return_one)
        rho_k0 = property(return_one)
        rho_gamma0 = property(return_one)
        rho_nu0 = property(return_one)

        scale_factor = return_1arg
        H = return_1arg
        efunc = return_1arg
        inv_efunc = return_1arg
        Otot = return_1arg
        Om = return_1arg
        Ob = return_1arg
        Odm = return_1arg
        Ok = return_1arg
        Ode = return_1arg
        Ogamma = return_1arg
        Onu = return_1arg

        rho_critical = return_1arg
        rho_tot = return_1arg
        rho_m = return_1arg
        rho_de = return_1arg
        rho_k = return_1arg

        age = return_1arg
        lookback_time = return_1arg
        comoving_distance = return_1arg
        comoving_transverse_distance = return_1arg
        comoving_volume = return_1arg
        differential_comoving_volume = return_1arg

        angular_diameter_distance = return_1arg
        luminosity_distance = return_1arg

    cosmo = FLRW()

    assert isinstance(cosmo, FLRWAPIConformant)


def test_fixture(flrw: FLRWAPIConformant):
    """
    Test that the ``flrw`` fixture is a
    `cosmology.api.FLRWAPIConformant`.
    """
    assert isinstance(flrw, FLRWAPIConformant)
