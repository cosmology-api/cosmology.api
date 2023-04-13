"""Test ``cosmology.api.BaryonComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import BaryonComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_baryoncomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.BaryonComponent`.
    """
    # Simple example: missing everything

    class ExampleBaryonComponent:
        pass

    cosmo = ExampleBaryonComponent()

    assert not isinstance(cosmo, BaryonComponent)

    # TODO: more examples?


def test_compliant_baryoncomponent(matter_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.BaryonComponent`.
    """
    ExampleBaryonComponent = make_dataclass(
        "ExampleBaryonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_b0"}],
        bases=(matter_cls,),
        namespace={"Omega_b": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleBaryonComponent()

    assert isinstance(cosmo, BaryonComponent)


def test_fixture(baryon_cls):
    """
    Test that the ``baryon_cls`` fixture is a
    `cosmology.api.BaryonComponent`.
    """
    assert isinstance(baryon_cls(), BaryonComponent)
