"""Test ``cosmology.api.HasNeutrinoComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasNeutrinoComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_neutrinocomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasNeutrinoComponent`.
    """
    # Simple example: missing everything

    class ExampleHasNeutrinoComponent:
        pass

    cosmo = ExampleHasNeutrinoComponent()

    assert not isinstance(cosmo, HasNeutrinoComponent)

    # TODO: more examples?


def test_compliant_neutrinocomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasNeutrinoComponent`.
    """
    ExampleHasNeutrinoComponent = make_dataclass(
        "ExampleHasNeutrinoComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Neff", "m_nu"}],
        bases=(bkg_flrw_cls,),
        namespace={"Omega_nu0": _return_one, "Omega_nu": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasNeutrinoComponent()

    assert isinstance(cosmo, HasNeutrinoComponent)


def test_fixture(neutrino_cls):
    """
    Test that the ``neutrino_cls`` fixture is a
    `cosmology.api.HasNeutrinoComponent`.
    """
    assert isinstance(neutrino_cls(), HasNeutrinoComponent)
