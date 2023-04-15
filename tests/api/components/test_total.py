"""Test ``cosmology.api.HasTotalComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasTotalComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_totalcomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasTotalComponent`.
    """
    # Simple example: missing everything

    class ExampleHasTotalComponent:
        pass

    cosmo = ExampleHasTotalComponent()

    assert not isinstance(cosmo, HasTotalComponent)

    # TODO: more examples?


def test_compliant_totalomponent(comptotal_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasTotalComponent`.
    """
    ExampleHasTotalComponent = make_dataclass(
        "ExampleHasTotalComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_tot0"}],
        bases=(comptotal_cls,),
        namespace={"Omega_tot": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasTotalComponent()

    assert isinstance(cosmo, HasTotalComponent)


def test_fixture(comptotal_cls):
    """
    Test that the ``comptotal_cls`` fixture is a
    `cosmology.api.HasTotalComponent`.
    """
    assert isinstance(comptotal_cls(), HasTotalComponent)
