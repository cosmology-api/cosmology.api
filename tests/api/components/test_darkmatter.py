"""Test ``cosmology.api.HasDarkMatterComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasDarkMatterComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_darkmattercomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasDarkMatterComponent`.
    """
    # Simple example: missing everything

    class ExampleHasDarkMatterComponent:
        pass

    cosmo = ExampleHasDarkMatterComponent()

    assert not isinstance(cosmo, HasDarkMatterComponent)

    # TODO: more examples?


def test_compliant_darkmattercomponent(matter_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasDarkMatterComponent`.
    """
    ExampleHasDarkMatterComponent = make_dataclass(
        "ExampleHasDarkMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(matter_cls,),
        namespace={"Omega_dm0": _return_one, "Omega_dm": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasDarkMatterComponent()

    assert isinstance(cosmo, HasDarkMatterComponent)


def test_fixture(darkmatter_cls):
    """
    Test that the ``darkmatter_cls`` fixture is a
    `cosmology.api.HasDarkMatterComponent`.
    """
    assert isinstance(darkmatter_cls(), HasDarkMatterComponent)
