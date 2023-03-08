"""Test ``cosmology.api.HasDarkEnergyComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasDarkEnergyComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one  # noqa: F401

################################################################################
# TESTS
################################################################################


def test_noncompliant_darkenergycomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasDarkEnergyComponent`.
    """
    # Simple example: missing everything

    class ExampleHasDarkEnergyComponent:
        pass

    cosmo = ExampleHasDarkEnergyComponent()

    assert not isinstance(cosmo, HasDarkEnergyComponent)

    # TODO: more examples?


def test_compliant_darkenergycomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasDarkEnergyComponent`.
    """
    ExampleHasDarkEnergyComponent = make_dataclass(
        "ExampleHasDarkEnergyComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_de0"}],
        bases=(bkg_flrw_cls,),
        namespace={"Omega_de": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasDarkEnergyComponent()

    assert isinstance(cosmo, HasDarkEnergyComponent)


def test_fixture(darkenergy_cls):
    """
    Test that the ``darkenergy_cls`` fixture is a
    `cosmology.api.HasDarkEnergyComponent`.
    """
    assert isinstance(darkenergy_cls(), HasDarkEnergyComponent)
