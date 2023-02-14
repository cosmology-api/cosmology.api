"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import FriedmannLemaitreRobertsonWalker
from cosmology.api._array_api import Array

from .conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_bkg_flrw():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.FriedmannLemaitreRobertsonWalker`.
    """
    # Simple example: missing everything

    class FriedmannLemaitreRobertsonWalkerCosmology:
        pass

    cosmo = FriedmannLemaitreRobertsonWalkerCosmology()

    assert not isinstance(cosmo, FriedmannLemaitreRobertsonWalker)

    # TODO: more examples?


def test_compliant_bkg_flrw(bkg_flrw_cls, bkg_flrw_attrs, bkg_flrw_meths):
    """
    Test that an instance is `cosmology.api.FriedmannLemaitreRobertsonWalker` even if it
    doesn't inherit from `cosmology.api.FriedmannLemaitreRobertsonWalker`.
    """
    flds = set()

    FriedmannLemaitreRobertsonWalkerCosmology = make_dataclass(
        "FriedmannLemaitreRobertsonWalkerCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(bkg_flrw_cls,),
        namespace={n: property(_return_one) for n in bkg_flrw_attrs - set(flds)}
        | {n: _return_1arg for n in bkg_flrw_meths},
        frozen=True,
    )

    cosmo = FriedmannLemaitreRobertsonWalkerCosmology(name=None)

    assert isinstance(cosmo, FriedmannLemaitreRobertsonWalker)


def test_fixture(bkg_flrw):
    """
    Test that the ``bkg_flrw`` fixture is a
    `cosmology.api.FriedmannLemaitreRobertsonWalker`.
    """
    assert isinstance(bkg_flrw, FriedmannLemaitreRobertsonWalker)
