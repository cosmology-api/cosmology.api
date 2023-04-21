"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import make_dataclass

from cosmology.api import ComovingDistanceMeasures

from ..conftest import _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_dists():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.ComovingDistanceMeasures`.
    """
    # Simple example: missing everything

    class ComovingDistanceMeasuresCosmology:
        pass

    cosmo = ComovingDistanceMeasuresCosmology()

    assert not isinstance(cosmo, ComovingDistanceMeasures)

    # TODO: more examples?


def test_compliant_comoving(cosmology_cls):
    """Test that a compliant instance is a `cosmology.api.ComovingDistanceMeasures`."""
    ExampleComovingDistanceMeasures = make_dataclass(
        "ExampleComovingDistanceMeasures",
        [],
        bases=(cosmology_cls,),
        namespace={
            "comoving_distance": _return_1arg,
            "transverse_comoving_distance": _return_1arg,
            "comoving_volume": _return_1arg,
            "differential_comoving_volume": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleComovingDistanceMeasures()

    assert isinstance(cosmo, ComovingDistanceMeasures)


def test_fixture(comoving_cls):
    """Test that the ``comoving_cls`` fixture is a ``ComovingDistanceMeasures``."""
    assert isinstance(comoving_cls(), ComovingDistanceMeasures)
