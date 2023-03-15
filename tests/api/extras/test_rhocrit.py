"""Test ``cosmology.api.HasCriticalDensity``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasCriticalDensity
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hastcmbs():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasCriticalDensity`.
    """
    # Simple example: missing everything

    class ExampleHasCriticalDensity:
        pass

    cosmo = ExampleHasCriticalDensity()

    assert not isinstance(cosmo, HasCriticalDensity)

    # TODO: more examples?


def test_compliant_hastcmbs(hasrhocrit_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasCriticalDensity`.
    """
    ExampleHasCriticalDensity = make_dataclass(
        "ExampleHasCriticalDensity",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(hasrhocrit_cls,),
        namespace={
            "Tcmb0": _default_one,
            "Tcmb": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleHasCriticalDensity()

    assert isinstance(cosmo, HasCriticalDensity)


def test_fixture(hasrhocrit_cls):
    """
    Test that the ``hasrhocrit_cls`` fixture is a
    `cosmology.api.HasCriticalDensity`.
    """
    assert isinstance(hasrhocrit_cls(), HasCriticalDensity)
