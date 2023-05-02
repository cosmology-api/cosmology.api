"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import make_dataclass

from cosmology.api import ProperDistanceMeasures

from ..conftest import _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_dists():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.ProperDistanceMeasures`.
    """
    # Simple example: missing everything

    class ProperDistanceMeasuresCosmology:
        pass

    cosmo = ProperDistanceMeasuresCosmology()

    assert not isinstance(cosmo, ProperDistanceMeasures)

    # TODO: more examples?


def test_compliant_comoving(cosmology_cls):
    """Test that a compliant instance is a `cosmology.api.ProperDistanceMeasures`."""
    ExampleProperDistanceMeasures = make_dataclass(
        "ExampleProperDistanceMeasures",
        [],
        bases=(cosmology_cls,),
        namespace={
            "proper_distance": _return_1arg,
            "proper_time": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleProperDistanceMeasures()

    assert isinstance(cosmo, ProperDistanceMeasures)


def test_fixture(proper_cls):
    """Test that the ``proper_cls`` fixture is a ``ProperDistanceMeasures``."""
    assert isinstance(proper_cls(), ProperDistanceMeasures)
