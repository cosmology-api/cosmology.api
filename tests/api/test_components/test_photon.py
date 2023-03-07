"""Test ``cosmology.api.PhotonComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import PhotonComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_photoncomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.PhotonComponent`.
    """
    # Simple example: missing everything

    class ExamplePhotonComponent:
        pass

    cosmo = ExamplePhotonComponent()

    assert not isinstance(cosmo, PhotonComponent)

    # TODO: more examples?


def test_compliant_photoncomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.PhotonComponent`.
    """
    ExamplePhotonComponent = make_dataclass(
        "ExamplePhotonComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {}],
        bases=(bkg_flrw_cls,),
        namespace={"Ogamma0": _return_one, "Ogamma": _return_1arg},
        frozen=True,
    )

    cosmo = ExamplePhotonComponent()

    assert isinstance(cosmo, PhotonComponent)


def test_fixture(photon_cls):
    """
    Test that the ``photon_cls`` fixture is a
    `cosmology.api.PhotonComponent`.
    """
    assert isinstance(photon_cls(), PhotonComponent)
