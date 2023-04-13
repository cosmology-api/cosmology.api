"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasDistanceMeasures
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_dists():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasDistanceMeasures`.
    """
    # Simple example: missing everything

    class HasDistanceMeasuresCosmology:
        pass

    cosmo = HasDistanceMeasuresCosmology()

    assert not isinstance(cosmo, HasDistanceMeasures)

    # TODO: more examples?


def test_compliant_dists(dists_cls, dists_attrs, dists_meths):
    """
    Test that an instance is `cosmology.api.HasDistanceMeasures` even if it
    doesn't inherit from `cosmology.api.HasDistanceMeasures`.
    """
    flds = set()

    HasDistanceMeasuresCosmology = make_dataclass(
        "HasDistanceMeasuresCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(dists_cls,),
        namespace={n: property(_return_one) for n in dists_attrs - set(flds)}
        | {n: _return_1arg for n in dists_meths},
        frozen=True,
    )

    cosmo = HasDistanceMeasuresCosmology()

    assert isinstance(cosmo, HasDistanceMeasures)


def test_fixture(dists):
    """
    Test that the ``dists`` fixture is a
    `cosmology.api.HasDistanceMeasures`.
    """
    assert isinstance(dists, HasDistanceMeasures)
