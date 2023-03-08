"""Test ``cosmology.api.MatterComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import MatterComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_mattercomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.MatterComponent`.
    """
    # Simple example: missing everything

    class ExampleMatterComponent:
        pass

    cosmo = ExampleMatterComponent()

    assert not isinstance(cosmo, MatterComponent)

    # TODO: more examples?


def test_compliant_mattercomponent(bkg_flrw_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.MatterComponent`.
    """
    ExampleMatterComponent = make_dataclass(
        "ExampleMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_m0"}],
        bases=(bkg_flrw_cls,),
        namespace={"Omega_m": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleMatterComponent()

    assert isinstance(cosmo, MatterComponent)


def test_fixture(matter_cls):
    """
    Test that the ``matter_cls`` fixture is a
    `cosmology.api.MatterComponent`.
    """
    assert isinstance(matter_cls(), MatterComponent)
