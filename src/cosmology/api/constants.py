"""The cosmology constants API.

The list of required constants is:

- G: Gravitational constant G in pc km2 s-2 Msol-1.
- speed_of_light: Speed of light in km s-1.

"""

from __future__ import annotations

# STDLIB
from typing import Any, Protocol, runtime_checkable

__all__: list[str] = []


@runtime_checkable
class CosmologyConstantsAPINamespace(Protocol):
    """Cosmology constants API Protocol."""

    @property
    def G(self) -> Any:
        """Gravitational constant G in pc km2 s-2 Msol-1."""
        ...

    @property
    def speed_of_light(self) -> Any:
        """Speed of light in km s-1."""
        ...
