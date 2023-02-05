"""Test ``cosmology.api.DarkEnergyComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import DarkEnergyComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one  # noqa: F401

################################################################################
# TESTS
################################################################################


def test_noncompliant_darkenergycomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.DarkEnergyComponent`.
    """
    # Simple example: missing everything

    class ExampleDarkEnergyComponent:
        pass

    cosmo = ExampleDarkEnergyComponent()

    assert not isinstance(cosmo, DarkEnergyComponent)

    # TODO: more examples?


def test_compliant_darkenergycomponent(bkg_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.DarkEnergyComponent`.
    """
    ExampleDarkEnergyComponent = make_dataclass(
        "ExampleDarkEnergyComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Ode0"}],
        bases=(bkg_cls,),
        namespace={"Ode": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleDarkEnergyComponent()

    assert isinstance(cosmo, DarkEnergyComponent)


def test_fixture(darkenergy_cls):
    """
    Test that the ``darkenergy_cls`` fixture is a
    `cosmology.api.DarkEnergyComponent`.
    """
    assert isinstance(darkenergy_cls(), DarkEnergyComponent)
