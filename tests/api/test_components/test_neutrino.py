"""Test ``cosmology.api.NeutrinoComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import NeutrinoComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_neutrinocomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.NeutrinoComponent`.
    """
    # Simple example: missing everything

    class ExampleNeutrinoComponent:
        pass

    cosmo = ExampleNeutrinoComponent()

    assert not isinstance(cosmo, NeutrinoComponent)

    # TODO: more examples?


def test_compliant_neutrinocomponent(bkg_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.NeutrinoComponent`.
    """
    ExampleNeutrinoComponent = make_dataclass(
        "ExampleNeutrinoComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Neff", "m_nu"}],
        bases=(bkg_cls,),
        namespace={"Onu0": _return_one, "Onu": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleNeutrinoComponent()

    assert isinstance(cosmo, NeutrinoComponent)


def test_fixture(neutrino_cls):
    """
    Test that the ``neutrino_cls`` fixture is a
    `cosmology.api.NeutrinoComponent`.
    """
    assert isinstance(neutrino_cls(), NeutrinoComponent)
