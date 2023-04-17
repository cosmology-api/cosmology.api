"""Test ``cosmology.api.TemperatureCMB``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import TemperatureCMB
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hastcmbs():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.TemperatureCMB`.
    """
    # Simple example: missing everything

    class ExampleTemperatureCMB:
        pass

    cosmo = ExampleTemperatureCMB()

    assert not isinstance(cosmo, TemperatureCMB)

    # TODO: more examples?


def test_compliant_hastcmbs(bkgt_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.TemperatureCMB`.
    """
    ExampleTemperatureCMB = make_dataclass(
        "ExampleTemperatureCMB",
        [(n, Array, field(default_factory=_default_one)) for n in {"T_cmb0"}],
        bases=(bkgt_cls,),
        namespace={"T_cmb": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleTemperatureCMB()

    assert isinstance(cosmo, TemperatureCMB)


def test_fixture(bkgt_cls):
    """
    Test that the ``bkgt_cls`` fixture is a
    `cosmology.api.TemperatureCMB`.
    """
    assert isinstance(bkgt_cls(), TemperatureCMB)
