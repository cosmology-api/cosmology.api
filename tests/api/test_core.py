"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import dataclass

from cosmology.api import Cosmology, CosmologyNamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.Cosmology`.
    """
    # Simple example: missing everything

    class ExampleCosmology:
        pass

    cosmo = ExampleCosmology()

    assert not isinstance(cosmo, Cosmology)

    # TODO: more examples?


def test_compliant_cosmology(cosmology_ns):
    """
    Test that a compliant instance is a
    `cosmology.api.Cosmology`.
    """

    @dataclass
    class Cosmology:
        name: str | None = None

        @property
        def __cosmology_namespace__(self) -> CosmologyNamespace:
            return cosmology_ns

    cosmo = Cosmology()

    assert isinstance(cosmo, Cosmology)


def test_fixture(cosmology):
    """
    Test that the ``cosmology`` fixture is a
    `cosmology.api.Cosmology`.
    """
    assert isinstance(cosmology, Cosmology)
