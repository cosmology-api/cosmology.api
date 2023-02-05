"""Fixtures for the Cosmology API standard."""

from __future__ import annotations

import functools
import operator
from dataclasses import dataclass, field, fields, make_dataclass
from types import SimpleNamespace
from typing import TypeVar

import numpy.array_api as xp
import pytest
from cosmology.api import (
    BackgroundCosmologyAPI,
    CosmologyAPI,
    CosmologyAPINamespace,
    CosmologyConstantsAPINamespace,
    StandardCosmologyAPI,
)
from cosmology.api._array_api import Array
from cosmology.api.background import BACKGROUNDCOSMO_ATTRIBUTES, BACKGROUNDCOSMO_METHODS
from cosmology.api.components import (
    BaryonComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    GlobalCurvatureComponent,
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
)
from cosmology.api.standard import STANDARDCOSMO_ATTRIBUTES, STANDARDCOSMO_METHODS

CT = TypeVar("CT", bound=CosmologyAPI)


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

        name: str | None = None  # normally has a default, but not for testing

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
def cosmology(cosmology_cls: type[CosmologyAPI]) -> CosmologyAPI:
    """An example cosmology API instance."""
    return cosmology_cls(name=None)


# ==============================================================================
# COMPONENTS API


def get_comp_attrs(comp_cls: type) -> set[str]:
    """The attributes of a component."""
    methods_and_attrs = set(dir(comp_cls)) - set(dir(CosmologyAPI))

    return {k for k in methods_and_attrs if not callable(getattr(comp_cls, k))}


def get_comp_meths(comp_cls: type) -> set[str]:
    """The attributes of a component."""
    methods_and_attrs = set(dir(comp_cls)) - set(dir(CosmologyAPI))

    return {k for k in methods_and_attrs if callable(getattr(comp_cls, k))}


@pytest.fixture(scope="session")
def globalcurvature_cls(
    cosmology_cls: type[CosmologyAPI],
) -> type[GlobalCurvatureComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(GlobalCurvatureComponent)
    comp_meths = get_comp_meths(GlobalCurvatureComponent)
    fields = set()  # Ok0 is not a field
    return make_dataclass(
        "ExampleGlobalCurvatureComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - fields}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def matter_cls(
    cosmology_cls: type[CosmologyAPI],
) -> type[MatterComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(MatterComponent)
    comp_meths = get_comp_meths(MatterComponent)
    fields = {"Om0"}
    return make_dataclass(
        "ExampleMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def baryon_cls(matter_cls: type[CosmologyAPI]) -> type[BaryonComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(BaryonComponent)
    comp_meths = get_comp_meths(BaryonComponent)
    flds = {f.name for f in fields(matter_cls)} | {"Ob0"}
    return make_dataclass(
        "ExampleBaryonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(matter_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(flds)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def darkmatter_cls(
    matter_cls: type[CosmologyAPI],
) -> type[DarkMatterComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(DarkMatterComponent)
    comp_meths = get_comp_meths(DarkMatterComponent)
    flds = {f.name for f in fields(matter_cls)}  # Odm0 is not a field
    return make_dataclass(
        "ExampleDarkMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(matter_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(flds)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def neutrino_cls(
    cosmology_cls: type[CosmologyAPI],
) -> type[NeutrinoComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(NeutrinoComponent)
    comp_meths = get_comp_meths(NeutrinoComponent)
    fields = {"Neff", "m_nu"}
    return make_dataclass(
        "ExampleNeutrinoComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
@pytest.mark.parametrize("comp_cls", [PhotonComponent])
def photon_cls(
    cosmology_cls: type[CosmologyAPI],
) -> type[PhotonComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(PhotonComponent)
    comp_meths = get_comp_meths(PhotonComponent)
    fields = set()  # Ogamma0 is not a field
    return make_dataclass(
        "ExamplePhotonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
@pytest.mark.parametrize("comp_cls", [DarkEnergyComponent])
def darkenergy_cls(
    cosmology_cls: type[CosmologyAPI],
) -> type[DarkEnergyComponent | CosmologyAPI]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(DarkEnergyComponent)
    comp_meths = get_comp_meths(DarkEnergyComponent)
    fields = {"Ode0"}
    return make_dataclass(
        "ExampleDarkEnergyComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


# ==============================================================================
# Background API


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
    """An example Background class."""
    flds = set()  # there are no fields
    return make_dataclass(
        "ExampleBackgroundCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in background_attrs - flds}
        | {n: _return_1arg for n in background_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def bkg(bkg_cls: type[BackgroundCosmologyAPI]) -> BackgroundCosmologyAPI:
    """An example FLRW API instance."""
    return bkg_cls()


# ==============================================================================
# Standard API


@pytest.fixture(scope="session")
def standard_attrs() -> frozenset[str]:
    """The Standard FLRW API atributes."""
    return STANDARDCOSMO_ATTRIBUTES


@pytest.fixture(scope="session")
def standard_meths() -> frozenset[str]:
    """The Standard FLRW API methods."""
    return STANDARDCOSMO_METHODS


@pytest.fixture(scope="session")
def standard_cls(  # noqa: PLR0913
    bkg_cls: type[BackgroundCosmologyAPI],
    globalcurvature_cls: type[GlobalCurvatureComponent],
    matter_cls: type[MatterComponent],
    baryon_cls: type[BaryonComponent],
    darkmatter_cls: type[DarkMatterComponent],
    neutrino_cls: type[NeutrinoComponent],
    photon_cls: type[PhotonComponent],
    darkenergy_cls: type[DarkEnergyComponent],
    standard_attrs: set[str],
    standard_meths: set[str],
) -> type[StandardCosmologyAPI]:
    """Example FLRW API class."""
    bases = (
        neutrino_cls,
        photon_cls,
        darkenergy_cls,
        baryon_cls,
        darkmatter_cls,
        matter_cls,
        globalcurvature_cls,
        bkg_cls,
    )
    flds = functools.reduce(
        operator.or_, ({f.name for f in fields(c)} for c in bases)
    ) | {"H0"}

    return make_dataclass(
        "ExampleStandardCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=bases,  # only inherit from Background to not have the properties
        namespace={n: property(_return_one) for n in standard_attrs - flds}
        | {n: _return_1arg for n in standard_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def standardcosmo(
    standard_cls: type[StandardCosmologyAPI],
) -> StandardCosmologyAPI:
    """Example FLRW API instance."""
    return standard_cls()
