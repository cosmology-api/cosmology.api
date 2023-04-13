"""Test ``cosmology.api.BackgroundTemperature``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import ScaleFactor
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_scalefactor():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.BackgroundTemperature`.
    """
    # Simple example: missing everything

    class ExampleScaleFactor:
        pass

    cosmo = ExampleScaleFactor()

    assert not isinstance(cosmo, ScaleFactor)

    # TODO: more examples?


def test_compliant_scalefactor(scalefactor_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.BackgroundTemperature`.
    """
    ExampleScaleFactor = make_dataclass(
        "ExampleScaleFactor",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(scalefactor_cls,),
        namespace={
            "T_cmb0": _default_one,
            "Tcmb": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleScaleFactor()

    assert isinstance(cosmo, ScaleFactor)


def test_fixture(scalefactor_cls):
    """
    Test that the ``scalefactor_cls`` fixture is a
    `cosmology.api.ScaleFactor`.
    """
    assert isinstance(scalefactor_cls(), ScaleFactor)
