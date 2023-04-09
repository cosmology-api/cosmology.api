"""Test ``cosmology.api.core``."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from cosmology.api import Cosmology, CosmologyConstantsNamespace, CosmologyNamespace

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


def test_compliant_cosmology(cosmology_ns: CosmologyNamespace):
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

        @property
        def constants(self) -> CosmologyConstantsNamespace:
            return self.__cosmology_namespace__.constants

    cosmo = Cosmology()

    assert isinstance(cosmo, Cosmology)


def test_fixture(cosmology: Cosmology[Any, Any]):
    """
    Test that the ``cosmology`` fixture is a
    `cosmology.api.Cosmology`.
    """
    assert isinstance(cosmology, Cosmology)
