"""Test ``cosmology.api.BackgroundTemperature``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api._array_api import Array
from cosmology.api._distances import BackgroundTemperature

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hastcmbs():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.BackgroundTemperature`.
    """
    # Simple example: missing everything

    class ExampleBackgroundTemperature:
        pass

    cosmo = ExampleBackgroundTemperature()

    assert not isinstance(cosmo, BackgroundTemperature)

    # TODO: more examples?


def test_compliant_hastcmbs(bkgt_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.BackgroundTemperature`.
    """
    ExampleBackgroundTemperature = make_dataclass(
        "ExampleBackgroundTemperature",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(bkgt_cls,),
        namespace={
            "T_cmb0": _default_one,
            "Tcmb": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleBackgroundTemperature()

    assert isinstance(cosmo, BackgroundTemperature)


def test_fixture(bkgt_cls):
    """
    Test that the ``bkgt_cls`` fixture is a
    `cosmology.api.BackgroundTemperature`.
    """
    assert isinstance(bkgt_cls(), BackgroundTemperature)
