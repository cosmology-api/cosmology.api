"""Test ``cosmology.api.HasPhotonComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasPhotonComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_photoncomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasPhotonComponent`.
    """
    # Simple example: missing everything

    class ExampleHasPhotonComponent:
        pass

    cosmo = ExampleHasPhotonComponent()

    assert not isinstance(cosmo, HasPhotonComponent)

    # TODO: more examples?


def test_compliant_photoncomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasPhotonComponent`.
    """
    ExampleHasPhotonComponent = make_dataclass(
        "ExampleHasPhotonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(bkg_flrw_cls,),
        namespace={"Omega_gamma0": _return_one, "Omega_gamma": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasPhotonComponent()

    assert isinstance(cosmo, HasPhotonComponent)


def test_fixture(photon_cls):
    """
    Test that the ``photon_cls`` fixture is a
    `cosmology.api.HasPhotonComponent`.
    """
    assert isinstance(photon_cls(), HasPhotonComponent)
