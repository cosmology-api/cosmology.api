"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import make_dataclass

from cosmology.api import LookbackDistanceMeasures

from ..conftest import _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_dists():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.LookbackDistanceMeasures`.
    """
    # Simple example: missing everything

    class LookbackDistanceMeasuresCosmology:
        pass

    cosmo = LookbackDistanceMeasuresCosmology()

    assert not isinstance(cosmo, LookbackDistanceMeasures)

    # TODO: more examples?


def test_compliant_comoving(cosmology_cls):
    """Test that a compliant instance is a `cosmology.api.LookbackDistanceMeasures`."""
    ExampleLookbackDistanceMeasures = make_dataclass(
        "ExampleLookbackDistanceMeasures",
        [],
        bases=(cosmology_cls,),
        namespace={
            "lookback_distance": _return_1arg,
            "lookback_time": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleLookbackDistanceMeasures()

    assert isinstance(cosmo, LookbackDistanceMeasures)


def test_fixture(lookback_cls):
    """Test that the ``lookback_cls`` fixture is a ``LookbackDistanceMeasures``."""
    assert isinstance(lookback_cls(), LookbackDistanceMeasures)
