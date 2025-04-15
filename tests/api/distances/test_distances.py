"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import DistanceMeasures
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg, _return_one

################################################################################
# TESTS
################################################################################


def test_noncompliant_dists():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.DistanceMeasures`.
    """
    # Simple example: missing everything

    class DistanceMeasuresCosmology:
        pass

    cosmo = DistanceMeasuresCosmology()

    assert not isinstance(cosmo, DistanceMeasures)

    # TODO: more examples?


def test_compliant_dists(dists_cls, dists_attrs, dists_meths):
    """
    Test that an instance is `cosmology.api.DistanceMeasures` even if it
    doesn't inherit from `cosmology.api.DistanceMeasures`.
    """
    flds = set()

    DistanceMeasuresCosmology = make_dataclass(
        "DistanceMeasuresCosmology",
        [(n, Array, field(default_factory=_default_one)) for n in flds],
        bases=(dists_cls,),
        namespace={n: property(_return_one) for n in dists_attrs - set(flds)}
        | dict.fromkeys(dists_meths, _return_1arg),
        frozen=True,
    )

    cosmo = DistanceMeasuresCosmology()

    assert isinstance(cosmo, DistanceMeasures)


def test_fixture(dists):
    """
    Test that the ``dists`` fixture is a
    `cosmology.api.DistanceMeasures`.
    """
    assert isinstance(dists, DistanceMeasures)
