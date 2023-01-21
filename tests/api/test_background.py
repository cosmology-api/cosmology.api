"""Test ``cosmology_api.api.core``."""

from __future__ import annotations

# STDLIB
from dataclasses import field, make_dataclass

# THIRD-PARTY
import numpy.array_api as xp

# LOCAL
from cosmology.api import BackgroundCosmologyAPI
from cosmology.api._array_api import Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_bkg():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPI`.
    """
    # Simple example: missing everything

    class BackbroundCosmology:
        pass

    cosmo = BackbroundCosmology()

    assert not isinstance(cosmo, BackgroundCosmologyAPI)

    # TODO: more examples?


def test_compliant_bkg(cosmology_cls, background_attrs, background_meths):
    """
    Test that an instance is `cosmology.api.BackgroundCosmologyAPI` even if it
    doesn't inherit from `cosmology.api.BackgroundCosmologyAPI`.
    """

    def _default_one() -> Array:
        return xp.ones((), dtype=xp.int32)

    def _return_one(self, /) -> Array:
        return _default_one()

    def _return_1arg(self, z: Array, /) -> Array:
        return z

    fields = ()

    BackgroundCosmology = make_dataclass(
        "BackgroundCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in fields],
        bases=(cosmology_cls,),
        namespace={n: property(_return_one) for n in background_attrs - set(fields)}
        | {n: _return_1arg for n in background_meths},
        frozen=True,
    )

    cosmo = BackgroundCosmology()

    assert isinstance(cosmo, BackgroundCosmologyAPI)


def test_fixture(bkg):
    """
    Test that the ``bkg`` fixture is a
    `cosmology.api.BackgroundCosmologyAPI`.
    """
    assert isinstance(bkg, BackgroundCosmologyAPI)
