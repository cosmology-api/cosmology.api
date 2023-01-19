"""Fixtures for the Cosmology API standard."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass
from types import SimpleNamespace

# THIRD-PARTY
import pytest

# LOCAL
from cosmology.api import (
    CosmologyAPIConformant,
    CosmologyAPINamespace,
    CosmologyConstantsAPINamespace,
)


@pytest.fixture(scope="session")
def constants_ns() -> CosmologyConstantsAPINamespace:
    """The cosmology constants API namespace."""
    return SimpleNamespace(G=1)


@pytest.fixture(scope="session")
def cosmology_ns(constants_ns: CosmologyConstantsAPINamespace) -> CosmologyAPINamespace:
    """The cosmology API namespace."""
    return SimpleNamespace(constants=constants_ns)


@pytest.fixture(scope="session")
def cosmology_cls(cosmology_ns: CosmologyAPINamespace) -> CosmologyAPIConformant:
    """An example cosmology API class."""

    @dataclass(frozen=True)
    class ExampleCosmology(CosmologyAPIConformant):
        """An example cosmology API class."""

        name: str | None = None

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        # === not CosmologyAPI ===

        @property
        def not_cosmology_api(self) -> int:
            return 1

    return ExampleCosmology


@pytest.fixture(scope="session")
def cosmology(cosmology_cls: type[CosmologyAPIConformant]) -> CosmologyAPIConformant:
    """An example cosmology API instance."""
    return cosmology_cls()
