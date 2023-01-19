"""The Cosmology API Namespace."""

from __future__ import annotations

# STDLIB
from typing import Protocol, runtime_checkable

# LOCAL
from .constants import CosmologyConstantsAPINamespace

__all__: list[str] = []


@runtime_checkable
class CosmologyAPINamespace(Protocol):
    """Runtime-checkable Protocol for the Cosmology API namespace."""

    @property
    def constants(self) -> CosmologyConstantsAPINamespace:
        """The cosmology constants API."""
        ...
