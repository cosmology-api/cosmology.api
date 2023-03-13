"""The cosmology constants API.

The list of required constants is:

- G: Gravitational constant G in pc km2 s-2 Msol-1.
- c: Speed of light in km s-1.

"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

__all__: list[str] = []


@runtime_checkable
class CosmologyConstantsNamespace(Protocol):
    """Cosmology constants API Protocol."""

    @property
    def G(self) -> Any:  # noqa: ANN401
        """Gravitational constant G in pc km2 s-2 Msol-1."""
        ...

    @property
    def c(self) -> Any:  # noqa: ANN401
        """Speed of light in km s-1."""
        ...
