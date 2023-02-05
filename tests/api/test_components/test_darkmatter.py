"""Test ``cosmology.api.DarkMatterComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import DarkMatterComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_darkmattercomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.DarkMatterComponent`.
    """
    # Simple example: missing everything

    class ExampleDarkMatterComponent:
        pass

    cosmo = ExampleDarkMatterComponent()

    assert not isinstance(cosmo, DarkMatterComponent)

    # TODO: more examples?


def test_compliant_darkmattercomponent(matter_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.DarkMatterComponent`.
    """
    ExampleDarkMatterComponent = make_dataclass(
        "ExampleDarkMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(matter_cls,),
        namespace={"Odm0": _return_one, "Odm": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleDarkMatterComponent()

    assert isinstance(cosmo, DarkMatterComponent)


def test_fixture(darkmatter_cls):
    """
    Test that the ``darkmatter_cls`` fixture is a
    `cosmology.api.DarkMatterComponent`.
    """
    assert isinstance(darkmatter_cls(), DarkMatterComponent)
