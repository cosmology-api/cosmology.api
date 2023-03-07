"""Test ``cosmology.api.HasGlobalCurvatureComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasGlobalCurvatureComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_globalcurvaturecomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasGlobalCurvatureComponent`.
    """
    # Simple example: missing everything

    class ExampleHasGlobalCurvatureComponent:
        pass

    cosmo = ExampleHasGlobalCurvatureComponent()

    assert not isinstance(cosmo, HasGlobalCurvatureComponent)

    # TODO: more examples?


def test_compliant_globalcurvaturecomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasGlobalCurvatureComponent`.
    """
    ExampleHasGlobalCurvatureComponent = make_dataclass(
        "ExampleHasGlobalCurvatureComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(bkg_flrw_cls,),
        namespace={"Omega_k0": _return_one, "Omega_k": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasGlobalCurvatureComponent()

    assert isinstance(cosmo, HasGlobalCurvatureComponent)


def test_fixture(globalcurvature_cls):
    """
    Test that the ``globalcurvature_cls`` fixture is a
    `cosmology.api.HasGlobalCurvatureComponent`.
    """
    assert isinstance(globalcurvature_cls(), HasGlobalCurvatureComponent)
