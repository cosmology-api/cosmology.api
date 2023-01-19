"""Fixtures for the Cosmology API standard."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass, field, make_dataclass
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


def _default_one() -> Array:
    return xp.ones((), dtype=xp.int32)


def _return_one(self, /) -> Array:
    return _default_one()


def _return_1arg(self, z: Array, /) -> Array:
    return z


@pytest.fixture(scope="session")
def flrw_attrs() -> set[str]:
    """The FLRW API atributes."""
    return {
        "H0",
        "Om0",
        "Ode0",
        "Tcmb0",
        "Neff",
        "m_nu",
        "Ob0",
        "scale_factor0",
        "h",
        "hubble_distance",
        "hubble_time",
        "Otot0",
        "Odm0",
        "Ok0",
        "Ogamma0",
        "Onu0",
        "rho_critical0",
        "rho_tot0",
        "rho_m0",
        "rho_de0",
        "rho_b0",
        "rho_dm0",
        "rho_k0",
        "rho_gamma0",
        "rho_nu0",
    }


@pytest.fixture(scope="session")
def flrw_meths() -> set[str]:
    """The FLRW API methods."""
    return {
        "scale_factor",
        "H",
        "efunc",
        "inv_efunc",
        "Otot",
        "Om",
        "Ob",
        "Odm",
        "Ok",
        "Ode",
        "Ogamma",
        "Onu",
        "rho_critical",
        "rho_tot",
        "rho_m",
        "rho_de",
        "rho_k",
        "age",
        "lookback_time",
        "comoving_distance",
        "comoving_transverse_distance",
        "comoving_volume",
        "differential_comoving_volume",
        "angular_diameter_distance",
        "luminosity_distance",
    }


@pytest.fixture(scope="session")
def flrw_cls(
    cosmology_cls: type[CosmologyAPIConformant],
    flrw_attrs: set[str],
    flrw_meths: set[str],
) -> type[FLRWAPIConformant]:
    """An example FLRW API class."""
    fields = ("H0", "Om0", "Ode0", "Tcmb0", "Neff", "m_nu", "Ob0")

    return make_dataclass(
        "ExampleFLRW",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(FLRWAPIConformant, cosmology_cls),
        namespace={n: property(_return_one) for n in flrw_attrs - set(fields)}
        | {n: _return_1arg for n in flrw_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def flrw(flrw_cls: type[FLRWAPIConformant]) -> FLRWAPIConformant:
    """An example FLRW API instance."""
    return flrw_cls()


@pytest.fixture(scope="session")
def flrw_wrapper_cls(
    cosmology_wrapper_cls: type[CosmologyAPIConformantWrapper],
    flrw_attrs: set[str],
    flrw_meths: set[str],
) -> type[FLRWAPIConformantWrapper]:
    """An example FLRW API wrapper class."""
    return make_dataclass(
        "FLRWWrapper",
        [("cosmo", object)],
        bases=(cosmology_wrapper_cls, FLRWAPIConformantWrapper),
        namespace={n: property(_return_one) for n in flrw_attrs}
        | {n: _return_1arg for n in flrw_meths},
        frozen=True,
    )
