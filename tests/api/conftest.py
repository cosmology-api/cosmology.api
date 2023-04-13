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
    Cosmology,
    CosmologyConstantsNamespace,
    CosmologyNamespace,
    HasBaryonComponent,
    HasCriticalDensity,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasDistanceMeasures,
    HasGlobalCurvatureComponent,
    HasHubbleParameter,
    HasMatterComponent,
    HasNeutrinoComponent,
    HasPhotonComponent,
    StandardCosmology,
)
from cosmology.api._array_api import Array
from cosmology.api._distances import _HasTcmb

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

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyNamespace:
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


@pytest.fixture(scope="session")
def globalcurvature_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasGlobalCurvatureComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasGlobalCurvatureComponent)
    comp_meths = get_comp_meths(HasGlobalCurvatureComponent)
    fields = set()  # Omega_k0 is not a field
    return make_dataclass(
        "ExampleHasGlobalCurvatureComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - fields}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def matter_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasMatterComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasMatterComponent)
    comp_meths = get_comp_meths(HasMatterComponent)
    fields = {"Omega_m0"}
    return make_dataclass(
        "ExampleHasMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def baryon_cls(
    matter_cls: type[Cosmology],
) -> type[HasBaryonComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasBaryonComponent)
    comp_meths = get_comp_meths(HasBaryonComponent)
    flds = {f.name for f in fields(matter_cls)} | {"Omega_b0"}
    return make_dataclass(
        "ExampleHasBaryonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(matter_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(flds)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def darkmatter_cls(
    matter_cls: type[Cosmology],
) -> type[HasDarkMatterComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasDarkMatterComponent)
    comp_meths = get_comp_meths(HasDarkMatterComponent)
    flds = {f.name for f in fields(matter_cls)}  # Omega_dm0 is not a field
    return make_dataclass(
        "ExampleHasDarkMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(matter_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(flds)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def neutrino_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasNeutrinoComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasNeutrinoComponent)
    comp_meths = get_comp_meths(HasNeutrinoComponent)
    fields = {"Neff", "m_nu"}
    return make_dataclass(
        "ExampleHasNeutrinoComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def photon_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasPhotonComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasPhotonComponent)
    comp_meths = get_comp_meths(HasPhotonComponent)
    fields = set()  # Omega_gamma0 is not a field
    return make_dataclass(
        "ExampleHasPhotonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
@pytest.mark.parametrize("comp_cls", [HasDarkEnergyComponent])
def darkenergy_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasDarkEnergyComponent | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasDarkEnergyComponent)
    comp_meths = get_comp_meths(HasDarkEnergyComponent)
    fields = {"Omega_de0"}
    return make_dataclass(
        "ExampleHasDarkEnergyComponent",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


# ==============================================================================
# Parametrizations API


@pytest.fixture(scope="session")
def hashubbleparamet_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasHubbleParameter | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasHubbleParameter)
    comp_meths = get_comp_meths(HasHubbleParameter)
    fields = {"H0"}
    return make_dataclass(
        "ExampleHasHubbleParameter",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


@pytest.fixture(scope="session")
def hasrhocrit_cls(
    cosmology_cls: type[Cosmology],
) -> type[HasCriticalDensity | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(HasCriticalDensity)
    comp_meths = get_comp_meths(HasCriticalDensity)
    fields = {}
    return make_dataclass(
        "ExampleHasCriticalDensity",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


# ==============================================================================
# Distance Measures API


@pytest.fixture(scope="session")
def hastcmb_cls(
    cosmology_cls: type[Cosmology],
) -> type[_HasTcmb | Cosmology]:
    """An example standard cosmology API class."""
    comp_attrs = get_comp_attrs(_HasTcmb)
    comp_meths = get_comp_meths(_HasTcmb)
    fields = {"T_cmb0"}
    return make_dataclass(
        "Example_HasTcmb",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in comp_attrs - set(fields)}
        | {n: _return_1arg for n in comp_meths},
        frozen=True,
    )


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
    globalcurvature_cls: type[HasGlobalCurvatureComponent],
    matter_cls: type[HasMatterComponent],
    baryon_cls: type[HasBaryonComponent],
    darkmatter_cls: type[HasDarkMatterComponent],
    neutrino_cls: type[HasNeutrinoComponent],
    photon_cls: type[HasPhotonComponent],
    darkenergy_cls: type[HasDarkEnergyComponent],
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
