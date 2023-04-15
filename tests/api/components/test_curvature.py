"""Test ``cosmology.api.CurvatureComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import CurvatureComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_globalcurvaturecomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CurvatureComponent`.
    """
    # Simple example: missing everything

    class ExampleCurvatureComponent:
        pass

    cosmo = ExampleCurvatureComponent()

    assert not isinstance(cosmo, CurvatureComponent)

    # TODO: more examples?


def test_compliant_globalcurvaturecomponent(dists_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.CurvatureComponent`.
    """
    ExampleCurvatureComponent = make_dataclass(
        "ExampleCurvatureComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(dists_cls,),
        namespace={"Omega_k0": _return_one, "Omega_k": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleCurvatureComponent()

    assert isinstance(cosmo, CurvatureComponent)


def test_fixture(globalcurvature_cls):
    """
    Test that the ``globalcurvature_cls`` fixture is a
    `cosmology.api.CurvatureComponent`.
    """
    assert isinstance(globalcurvature_cls(), CurvatureComponent)
