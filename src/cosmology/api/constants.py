"""The cosmology constants API."""

# STDLIB
from typing import Any, Protocol, runtime_checkable

__all__: list[str] = []


@runtime_checkable
class CosmologyConstantsAPINamespace(Protocol):
    """Cosmology constants API Protocol."""

    @property
    def G(self) -> Any:  # noqa: N802
        """Gravitational constant G in pc km2 s-2 Msol-1."""
        ...
