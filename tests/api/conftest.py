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
    BackgroundCosmologyAPI,
    BackgroundCosmologyWrapperAPI,
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyConstantsAPINamespace,
    CosmologyWrapperAPI,
    StandardCosmologyAPI,
    StandardCosmologyWrapperAPI,
)
from cosmology.api._array_api import Array
from cosmology.api.background import BACKGROUNDCOSMO_ATTRIBUTES, BACKGROUNDCOSMO_METHODS
from cosmology.api.standard import STANDARDCOSMO_ATTRIBUTES, STANDARDCOSMO_METHODS

# ==============================================================================
# Library API


@pytest.fixture(scope="session")
def constants_ns() -> CosmologyConstantsAPINamespace:
    """The cosmology constants API namespace."""
    return SimpleNamespace(G=1, c=2)


@pytest.fixture(scope="session")
def cosmology_ns(constants_ns: CosmologyConstantsAPINamespace) -> CosmologyAPINamespace:
    """The cosmology API namespace."""
    return SimpleNamespace(constants=constants_ns)


# ==============================================================================
# Cosmology API


@pytest.fixture(scope="session")
def cosmology_cls(cosmology_ns: CosmologyAPINamespace) -> type[CosmologyAPI]:
    """An example cosmology API class."""

    @dataclass(frozen=True)
    class ExampleCosmology(CosmologyAPI):
        """An example cosmology API class."""

        name: str | None = None

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None,
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        # === not CosmologyAPI ===

        @property
        def not_cosmology_api(self) -> int:
            return 1

    return ExampleCosmology


@pytest.fixture(scope="session")
def cosmology(cosmology_cls: type[CosmologyAPI]) -> CosmologyAPI:
    """An example cosmology API instance."""
    return cosmology_cls()


@pytest.fixture(scope="session")
def cosmology_wrapper_cls(
    cosmology_ns: CosmologyAPINamespace,
) -> type[CosmologyWrapperAPI]:
    """An example cosmology API wrapper class."""

    @dataclass(frozen=True)
    class CosmologyWrapperAPI(CosmologyWrapperAPI):
        """An example cosmology API wrapper class."""

        cosmo: object

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None,
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

    return CosmologyWrapperAPI


# ==============================================================================
# FLRW API


def _default_one() -> Array:
    return xp.ones((), dtype=xp.int32)


def _return_one(self, /) -> Array:
    return _default_one()


def _return_1arg(self, z: Array, /) -> Array:
    return z


@pytest.fixture(scope="session")
def background_attrs() -> frozenset[str]:
    """The FLRW API atributes."""
    return BACKGROUNDCOSMO_ATTRIBUTES


@pytest.fixture(scope="session")
def background_meths() -> frozenset[str]:
    """The FLRW API methods."""
    return BACKGROUNDCOSMO_METHODS


@pytest.fixture(scope="session")
def bkg_cls(
    cosmology_cls: type[CosmologyAPI],
    background_attrs: set[str],
    background_meths: set[str],
) -> type[BackgroundCosmologyAPI]:
    """An example FLRW API class."""
    fields = ("H0",)

    return make_dataclass(
        "ExampleFLRW",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in background_attrs - set(fields)}
        | {n: _return_1arg for n in background_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def bkg(bkg_cls: type[BackgroundCosmologyAPI]) -> BackgroundCosmologyAPI:
    """An example FLRW API instance."""
    return bkg_cls()


@pytest.fixture(scope="session")
def bkg_wrapper_cls(
    cosmology_wrapper_cls: type[CosmologyWrapperAPI],
    background_attrs: set[str],
    background_meths: set[str],
) -> type[BackgroundCosmologyWrapperAPI]:
    """An example FLRW API wrapper class."""
    return make_dataclass(
        "FLRWWrapper",
        [("cosmo", object)],
        bases=(cosmology_wrapper_cls, BackgroundCosmologyWrapperAPI),
        namespace={n: property(_return_one) for n in background_attrs}
        | {n: _return_1arg for n in background_meths},
        frozen=True,
    )


# ==============================================================================
# Standard FLRW API


@pytest.fixture(scope="session")
def standard_attrs() -> frozenset[str]:
    """The Standard FLRW API atributes."""
    return STANDARDCOSMO_ATTRIBUTES


@pytest.fixture(scope="session")
def standard_meths() -> frozenset[str]:
    """The Standard FLRW API methods."""
    return STANDARDCOSMO_METHODS


@pytest.fixture(scope="session")
def standardbkg_cls(
    bkg_cls: type[BackgroundCosmologyAPI],
    standard_attrs: set[str],
    standard_meths: set[str],
) -> type[StandardCosmologyAPI]:
    """An example FLRW API class."""
    fields = ("H0", "Om0", "Ode0", "Tcmb0", "Neff", "m_nu", "Ob0")

    return make_dataclass(
        "ExampleFLRW",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(bkg_cls,),
        namespace={n: property(_return_one) for n in standard_attrs - set(fields)}
        | {n: _return_1arg for n in standard_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def standardcosmo(
    standardbkg_cls: type[StandardCosmologyAPI],
) -> StandardCosmologyAPI:
    """An example FLRW API instance."""
    return standardbkg_cls()


@pytest.fixture(scope="session")
def standardcosmo_wrapper_cls(
    bkg_wrapper_cls: type[BackgroundCosmologyWrapperAPI],
    background_attrs: set[str],
    background_meths: set[str],
) -> type[StandardCosmologyWrapperAPI]:
    """An example FLRW API wrapper class."""
    return make_dataclass(
        "FLRWWrapper",
        [("cosmo", object)],
        bases=(bkg_wrapper_cls, StandardCosmologyWrapperAPI),
        namespace={n: property(_return_one) for n in background_attrs}
        | {n: _return_1arg for n in background_meths},
        frozen=True,
    )
