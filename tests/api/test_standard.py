"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import Array
from cosmology.api._background import FriedmannLemaitreRobertsonWalker
from cosmology.api._components import (
    HasBaryonComponent,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasGlobalCurvatureComponent,
    HasMatterComponent,
    HasNeutrinoComponent,
    HasPhotonComponent,
)
from cosmology.api._core import CosmologyAPI
from cosmology.api._extras import HasHubbleParameter, HasTcmb

from .conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_standard():
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


def test_compliant_standard(cosmology_cls, standard_attrs, standard_meths):
    """
    Test that an instance is `cosmology.api.StandardCosmologyAPI` even if it
    doesn't inherit from `cosmology.api.StandardCosmologyAPI`.
    """
    fields = ("H0", "Omega_m0", "Omega_de0", "Tcmb0", "Neff", "m_nu", "Omega_b0")

    StandardCosmology = make_dataclass(
        "StandardCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in standard_attrs - set(fields)}
        | {n: _return_1arg for n in standard_meths},
        frozen=True,
    )

    cosmo = StandardCosmology()

    # Check Base and Background
    assert isinstance(cosmo, CosmologyAPI)
    assert isinstance(cosmo, FriedmannLemaitreRobertsonWalker)

    # Check Components
    assert isinstance(cosmo, HasBaryonComponent)
    assert isinstance(cosmo, HasDarkEnergyComponent)
    assert isinstance(cosmo, HasDarkMatterComponent)
    assert isinstance(cosmo, HasGlobalCurvatureComponent)
    assert isinstance(cosmo, HasMatterComponent)
    assert isinstance(cosmo, HasNeutrinoComponent)
    assert isinstance(cosmo, HasPhotonComponent)

    # Check Parametrizations
    assert isinstance(cosmo, HasHubbleParameter)
    assert isinstance(cosmo, HasTcmb)

    # Full Standard Cosmology
    assert isinstance(cosmo, StandardCosmologyAPI)


def test_fixture(standardcosmo):
    """
    Test that the ``standardcosmo`` fixture is a
    `cosmology.api.StandardCosmologyAPI`.
    """
    assert isinstance(standardcosmo, StandardCosmologyAPI)
