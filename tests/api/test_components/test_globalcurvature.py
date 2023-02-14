"""Test ``cosmology.api.GlobalCurvatureComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import GlobalCurvatureComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_globalcurvaturecomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.GlobalCurvatureComponent`.
    """
    # Simple example: missing everything

    class ExampleGlobalCurvatureComponent:
        pass

    cosmo = ExampleGlobalCurvatureComponent()

    assert not isinstance(cosmo, GlobalCurvatureComponent)

    # TODO: more examples?


def test_compliant_globalcurvaturecomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.GlobalCurvatureComponent`.
    """
    ExampleGlobalCurvatureComponent = make_dataclass(
        "ExampleGlobalCurvatureComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(bkg_flrw_cls,),
        namespace={"Ok0": _return_one, "Ok": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleGlobalCurvatureComponent()

    assert isinstance(cosmo, GlobalCurvatureComponent)


def test_fixture(globalcurvature_cls):
    """
    Test that the ``globalcurvature_cls`` fixture is a
    `cosmology.api.GlobalCurvatureComponent`.
    """
    assert isinstance(globalcurvature_cls(), GlobalCurvatureComponent)
