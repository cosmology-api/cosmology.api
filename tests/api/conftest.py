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
    BaryonComponent,
    Cosmology,
    CosmologyConstantsNamespace,
    CosmologyNamespace,
    CurvatureComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    HasBackgroundTemperature,
    HasCriticalDensityMethods,
    HasDistanceMeasures,
    HasHubbleMethods,
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
    StandardCosmology,
    TotalComponent,
)
from cosmology.api._array_api import Array

CT = TypeVar("CT", bound=Cosmology)


def _default_one() -> Array:
    return xp.ones((), dtype=xp.int32)


def _return_one(self, /) -> Array:
    return _default_one()


def _return_1arg(self, z: Array, /) -> Array:
    return z


def _get_attrs_meths(
    cls: type, comp_cls: type
) -> tuple[frozenset[str], frozenset[str]]:
    """Get the set of attributes and methods for a component class."""
    public_stuff = {
        k for k in (set(dir(cls)) - set(dir(comp_cls))) if not k.startswith("_")
    }
    attrs = frozenset({k for k in public_stuff if not callable(getattr(cls, k))})
    meths = frozenset({k for k in public_stuff if callable(getattr(cls, k))})
    return attrs, meths


# ==============================================================================
# Library API


@pytest.fixture(scope="session")
def constants_ns() -> CosmologyConstantsNamespace:
    """The cosmology constants API namespace."""
    return SimpleNamespace(G=1, c=2)


@pytest.fixture(scope="session")
def cosmology_ns(constants_ns: CosmologyConstantsNamespace) -> CosmologyNamespace:
    """The cosmology API namespace."""
    return SimpleNamespace(constants=constants_ns)


# ==============================================================================
# Cosmology API


@pytest.fixture(scope="session")
def cosmology_cls(cosmology_ns: CosmologyNamespace) -> type[Cosmology]:
    """An example cosmology API class."""

    @dataclass(frozen=True)
    class ExampleCosmology(Cosmology):
        """An example cosmology API class."""

        name: str | None = None  # normally has a default, but not for testing

        @property
        def __cosmology_namespace__(self) -> CosmologyNamespace:
            return cosmology_ns

        # === not Cosmology ===

        @property
        def not_cosmology_api(self) -> int:
            return 1

    return ExampleCosmology


@pytest.fixture(scope="session")
def cosmology(cosmology_cls: type[Cosmology]) -> Cosmology:
    """An example cosmology API instance."""
    return cosmology_cls(name=None)


# ==============================================================================
# COMPONENTS API


def get_comp_attrs(comp_cls: type) -> set[str]:
    """The attributes of a component."""
    methods_and_attrs = set(dir(comp_cls)) - set(dir(Cosmology))

    return {k for k in methods_and_attrs if not callable(getattr(comp_cls, k))}


def get_comp_meths(comp_cls: type) -> set[str]:
    """The attributes of a component."""
    methods_and_attrs = set(dir(comp_cls)) - set(dir(Cosmology))

    return {k for k in methods_and_attrs if callable(getattr(comp_cls, k))}


def make_comp_cls(
    comp_api_cls: type, fields: set[str], bases: tuple[type, ...]
) -> type:
    """Make a component class."""
    comp_attrs = get_comp_attrs(comp_api_cls)
    comp_meths = get_comp_meths(comp_api_cls)
    return make_dataclass(
        f"Example{comp_api_cls.__name__}",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=bases,
        namespace={n: property(_return_one) for n in comp_attrs - fields}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


# ----------------------------------


@pytest.fixture(scope="session")
def comptotal_cls(
    cosmology_cls: type[Cosmology],
) -> type[TotalComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(TotalComponent, {"Omega_tot0"}, bases=(cosmology_cls,))


@pytest.fixture(scope="session")
def globalcurvature_cls(
    cosmology_cls: type[Cosmology],
) -> type[CurvatureComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(CurvatureComponent, set(), bases=(cosmology_cls,))


@pytest.fixture(scope="session")
def matter_cls(
    cosmology_cls: type[Cosmology],
) -> type[MatterComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(MatterComponent, {"Omega_m0"}, bases=(cosmology_cls,))


@pytest.fixture(scope="session")
def baryon_cls(
    matter_cls: type[Cosmology],
) -> type[BaryonComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(BaryonComponent, {"Omega_b0"}, bases=(matter_cls,))


@pytest.fixture(scope="session")
def darkmatter_cls(
    matter_cls: type[Cosmology],
) -> type[DarkMatterComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(DarkMatterComponent, {"Omega_dm0"}, bases=(matter_cls,))


@pytest.fixture(scope="session")
def neutrino_cls(
    cosmology_cls: type[Cosmology],
) -> type[NeutrinoComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(NeutrinoComponent, {"Neff", "m_nu"}, bases=(cosmology_cls,))


@pytest.fixture(scope="session")
def photon_cls(
    cosmology_cls: type[Cosmology],
) -> type[PhotonComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(PhotonComponent, set(), bases=(cosmology_cls,))


@pytest.fixture(scope="session")
@pytest.mark.parametrize("comp_cls", [DarkEnergyComponent])
def darkenergy_cls(
    cosmology_cls: type[Cosmology],
) -> type[DarkEnergyComponent | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(DarkEnergyComponent, {"Omega_de0"}, bases=(cosmology_cls,))


# ==============================================================================
# Parametrizations API


@pytest.fixture(scope="session")
def hashubble_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasHubbleMethods | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(HasHubbleMethods, {"H0"}, bases=(cosmology_cls,))


@pytest.fixture(scope="session")
def hasrhocrit_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasCriticalDensityMethods | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(HasCriticalDensityMethods, set(), bases=(cosmology_cls,))


# ==============================================================================
# Distance Measures API


@pytest.fixture(scope="session")
def bkgt_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasBackgroundTemperature | Cosmology]:
    """An example standard cosmology API class."""
    return make_comp_cls(HasBackgroundTemperature, {"T_cmb0"}, bases=(cosmology_cls,))


DISTANCES_ATTRS, DISTANCES_METHS = _get_attrs_meths(HasDistanceMeasures, Cosmology)


@pytest.fixture(scope="session")
def dists_attrs() -> frozenset[str]:
    """The HasDistanceMeasures atributes."""
    return DISTANCES_ATTRS


@pytest.fixture(scope="session")
def dists_meths() -> frozenset[str]:
    """The HasDistanceMeasures methods."""
    return DISTANCES_METHS


@pytest.fixture(scope="session")
def dists_cls(
    cosmology_cls: type[Cosmology],
    dists_attrs: set[str],
    dists_meths: set[str],
) -> type[HasDistanceMeasures]:
    """An example Background class."""
    flds = set()  # there are no fields
    return make_dataclass(
        "ExampleHasDistanceMeasures",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in dists_attrs - flds}
        | {n: _return_1arg for n in dists_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def dists(
    dists_cls: type[HasDistanceMeasures],
) -> HasDistanceMeasures:
    """An example FLRW API instance."""
    return dists_cls()


# ==============================================================================
# Standard API


STDCOSMO_ATTRS, STDCOSMO_METHS = _get_attrs_meths(StandardCosmology, Cosmology)


@pytest.fixture(scope="session")
def standard_attrs() -> frozenset[str]:
    """The Standard FLRW API atributes."""
    return STDCOSMO_ATTRS


@pytest.fixture(scope="session")
def standard_meths() -> frozenset[str]:
    """The Standard FLRW API methods."""
    return STDCOSMO_METHS


@pytest.fixture(scope="session")
def standard_cls(  # noqa: PLR0913
    dists_cls: type[HasDistanceMeasures],
    globalcurvature_cls: type[CurvatureComponent],
    matter_cls: type[MatterComponent],
    baryon_cls: type[BaryonComponent],
    darkmatter_cls: type[DarkMatterComponent],
    neutrino_cls: type[NeutrinoComponent],
    photon_cls: type[PhotonComponent],
    darkenergy_cls: type[DarkEnergyComponent],
    standard_attrs: set[str],
    standard_meths: set[str],
) -> type[StandardCosmology]:
    """Example FLRW API class."""
    bases = (
        neutrino_cls,
        photon_cls,
        darkenergy_cls,
        baryon_cls,
        darkmatter_cls,
        matter_cls,
        globalcurvature_cls,
        dists_cls,
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
    standard_cls: type[StandardCosmology],
) -> StandardCosmology:
    """Example FLRW API instance."""
    return standard_cls()
