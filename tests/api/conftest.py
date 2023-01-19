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


@pytest.fixture()
def constants_ns() -> CosmologyConstantsAPINamespace:
    """The cosmology constants API namespace."""
    return SimpleNamespace(G=1)


@pytest.fixture()
def cosmology_ns(constants_ns: CosmologyConstantsAPINamespace) -> CosmologyAPINamespace:
    """The cosmology API namespace."""
    return SimpleNamespace(constants=constants_ns)


@pytest.fixture()
def cosmology_cls(cosmology_ns: CosmologyAPINamespace) -> CosmologyAPIConformant:
    """An example cosmology API class."""

    @dataclass
    class ExampleCosmology(CosmologyAPIConformant):
        """An example cosmology API class."""

        name: str | None = None

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

    return ExampleCosmology


@pytest.fixture()
def cosmology(cosmology_cls: type[CosmologyAPIConformant]) -> CosmologyAPIConformant:
    """An example cosmology API instance."""
    return cosmology_cls()
