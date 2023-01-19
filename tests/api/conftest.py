"""Fixtures for the Cosmology API standard."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass, field
from types import SimpleNamespace

# THIRD-PARTY
import numpy.array_api as xp
import pytest

# LOCAL
from cosmology.api import (
    CosmologyAPIConformant,
    CosmologyAPIConformantWrapper,
    CosmologyAPINamespace,
    CosmologyConstantsAPINamespace,
    FLRWAPIConformant,
    FLRWAPIConformantWrapper,
)
from cosmology.api._array_api.array import ArrayAPIConformant as Array

# ==============================================================================
# Library API


@pytest.fixture(scope="session")
def constants_ns() -> CosmologyConstantsAPINamespace:
    """The cosmology constants API namespace."""
    return SimpleNamespace(G=1)


@pytest.fixture(scope="session")
def cosmology_ns(constants_ns: CosmologyConstantsAPINamespace) -> CosmologyAPINamespace:
    """The cosmology API namespace."""
    return SimpleNamespace(constants=constants_ns)


# ==============================================================================
# Cosmology API


@pytest.fixture(scope="session")
def cosmology_cls(cosmology_ns: CosmologyAPINamespace) -> type[CosmologyAPIConformant]:
    """An example cosmology API class."""

    @dataclass(frozen=True)
    class ExampleCosmology(CosmologyAPIConformant):
        """An example cosmology API class."""

        name: str | None = None

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        # === not CosmologyAPI ===

        @property
        def not_cosmology_api(self) -> int:
            return 1

    return ExampleCosmology


@pytest.fixture(scope="session")
def cosmology(cosmology_cls: type[CosmologyAPIConformant]) -> CosmologyAPIConformant:
    """An example cosmology API instance."""
    return cosmology_cls()


@pytest.fixture(scope="session")
def cosmology_wrapper_cls(
    cosmology_ns: CosmologyAPINamespace,
) -> type[CosmologyAPIConformantWrapper]:
    """An example cosmology API wrapper class."""

    @dataclass(frozen=True)
    class CosmologyWrapper(CosmologyAPIConformantWrapper):
        """An example cosmology API wrapper class."""

        cosmo: object

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

    return CosmologyWrapper


# ==============================================================================
# FLRW API


@pytest.fixture(scope="session")
def flrw_cls(cosmology_cls: type[CosmologyAPIConformant]) -> type[FLRWAPIConformant]:
    """An example FLRW API class."""

    def default_one() -> Array:
        return xp.ones((), dtype=xp.int32)

    def return_one(self, /) -> Array:
        return default_one()

    def return_1arg(self, z: Array, /) -> Array:
        return z

    @dataclass(frozen=True)
    class ExampleFLRW(FLRWAPIConformant, cosmology_cls):

        H0: Array = field(default_factory=default_one)
        Om0: Array = field(default_factory=default_one)
        Ode0: Array = field(default_factory=default_one)
        Tcmb0: Array = field(default_factory=default_one)
        Neff: Array = field(default_factory=default_one)
        m_nu: Array = field(default_factory=default_one)
        Ob0: Array = field(default_factory=default_one)

        scale_factor0 = property(return_one)
        h = property(return_one)
        hubble_distance = property(return_one)
        hubble_time = property(return_one)
        Otot0 = property(return_one)
        Odm0 = property(return_one)
        Ok0 = property(return_one)
        Ogamma0 = property(return_one)
        Onu0 = property(return_one)

        critical_density0 = property(return_one)
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

    return ExampleFLRW


@pytest.fixture(scope="session")
def flrw(flrw_cls: type[FLRWAPIConformant]) -> FLRWAPIConformant:
    """An example FLRW API instance."""
    return flrw_cls(
        H0=1,
        Om0=1,
        Ode0=1,
        Tcmb0=1,
        Neff=1,
        m_nu=1,
        Ob0=1,
        name="example",
    )


@pytest.fixture(scope="session")
def flrw_wrapper_cls(
    cosmology_wrapper_cls: type[CosmologyAPIConformantWrapper],
) -> type[FLRWAPIConformantWrapper]:
    """An example FLRW API wrapper class."""

    def default_one() -> Array:
        return xp.ones((), dtype=xp.int32)

    def return_one(self, /) -> Array:
        return default_one()

    def return_1arg(self, z: Array, /) -> Array:
        return z

    @dataclass(frozen=True)
    class FLRWWrapper(cosmology_wrapper_cls, FLRWAPIConformantWrapper):
        """An example FLRW API wrapper class."""

        cosmo: object

        H0: Array = field(default_factory=default_one)
        Om0: Array = field(default_factory=default_one)
        Ode0: Array = field(default_factory=default_one)
        Tcmb0: Array = field(default_factory=default_one)
        Neff: Array = field(default_factory=default_one)
        m_nu: Array = field(default_factory=default_one)
        Ob0: Array = field(default_factory=default_one)

        scale_factor0 = property(return_one)
        h = property(return_one)
        hubble_distance = property(return_one)
        hubble_time = property(return_one)
        Otot0 = property(return_one)
        Odm0 = property(return_one)
        Ok0 = property(return_one)
        Ogamma0 = property(return_one)
        Onu0 = property(return_one)

        critical_density0 = property(return_one)
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

    return FLRWWrapper
