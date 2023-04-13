"""Test ``cosmology.api.TotalComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import TotalComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_totalcomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.TotalComponent`.
    """
    # Simple example: missing everything

    class ExampleTotalComponent:
        pass

    cosmo = ExampleTotalComponent()

    assert not isinstance(cosmo, TotalComponent)

    # TODO: more examples?


def test_compliant_totalomponent(comptotal_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.TotalComponent`.
    """
    ExampleTotalComponent = make_dataclass(
        "ExampleTotalComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_tot0"}],
        bases=(comptotal_cls,),
        namespace={"Omega_tot": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleTotalComponent()

    assert isinstance(cosmo, TotalComponent)


def test_fixture(comptotal_cls):
    """
    Test that the ``comptotal_cls`` fixture is a
    `cosmology.api.TotalComponent`.
    """
    assert isinstance(comptotal_cls(), TotalComponent)
