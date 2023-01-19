"""Test ``cosmology_api.api.core``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass

# LOCAL
from cosmology.api import CosmologyAPIConformant, CosmologyAPINamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPIConformant`.
    """
    # Simple example: missing everything

    class Cosmology:
        pass

    cosmo = Cosmology()

    assert not isinstance(cosmo, CosmologyAPIConformant)

    # TODO: more examples?


def test_compliant_cosmology(cosmology_ns):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyAPIConformant`.
    """

    @dataclass
    class Cosmology:
        name: str | None = None

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

    cosmo = Cosmology()

    assert isinstance(cosmo, CosmologyAPIConformant)


def test_fixture(cosmology):
    """
    Test that the ``cosmology`` fixture is a
    `cosmology.api.CosmologyAPIConformant`.
    """
    assert isinstance(cosmology, CosmologyAPIConformant)
