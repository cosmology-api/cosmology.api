"""Test ``cosmology.api.HasBaryonComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasBaryonComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_baryoncomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasBaryonComponent`.
    """
    # Simple example: missing everything

    class ExampleHasBaryonComponent:
        pass

    cosmo = ExampleHasBaryonComponent()

    assert not isinstance(cosmo, HasBaryonComponent)

    # TODO: more examples?


def test_compliant_baryoncomponent(matter_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasBaryonComponent`.
    """
    ExampleHasBaryonComponent = make_dataclass(
        "ExampleHasBaryonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_b0"}],
        bases=(matter_cls,),
        namespace={"Omega_b": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasBaryonComponent()

    assert isinstance(cosmo, HasBaryonComponent)


def test_fixture(baryon_cls):
    """
    Test that the ``baryon_cls`` fixture is a
    `cosmology.api.HasBaryonComponent`.
    """
    assert isinstance(baryon_cls(), HasBaryonComponent)
