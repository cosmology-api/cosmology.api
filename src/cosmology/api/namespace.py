"""The Cosmology API Namespace.

This module describes the namespace of a Cosmology-API compatible library. There
should be the following required objects:

- constants: a module of constants. See :mod:`cosmology.api.constants` for
  details.

"""

from __future__ import annotations

# STDLIB
from typing import Protocol, runtime_checkable

# LOCAL
from cosmology.api.constants import CosmologyConstantsAPINamespace

__all__: list[str] = []


@runtime_checkable
class CosmologyAPINamespace(Protocol):
    """Runtime-checkable Protocol for the Cosmology API namespace."""

    @property
    def constants(self) -> CosmologyConstantsAPINamespace:
        """The cosmology constants API."""
        ...
