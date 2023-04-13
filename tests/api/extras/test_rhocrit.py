"""Test ``cosmology.api.HasCriticalDensity``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import CriticalDensity
from cosmology.api._array_api import Array

from ..conftest import _default_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_hasrhocrit():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasCriticalDensity`.
    """
    # Simple example: missing everything

    class ExampleHasCriticalDensity:
        pass

    cosmo = ExampleHasCriticalDensity()

    assert not isinstance(cosmo, CriticalDensity)

    # TODO: more examples?


def test_compliant_hasrhocrit(cosmology_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasCriticalDensity`.
    """
    fields = {"critical_density0"}
    ExampleCriticalDensity = make_dataclass(
        "ExampleCriticalDensity",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={
            "critical_density": _default_one,
        },
        frozen=True,
    )

    cosmo = ExampleCriticalDensity()

    assert isinstance(cosmo, CriticalDensity)


def test_fixture(rhocrit_cls):
    """
    Test that the ``rhocrit_cls`` fixture is a
    `cosmology.api.CriticalDensity`.
    """
    assert isinstance(rhocrit_cls(), CriticalDensity)
