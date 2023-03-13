"""The Cosmology API Namespace.

This module describes the namespace of a Cosmology-API compatible library. There
should be the following required objects:

- constants: a module of constants. See :mod:`cosmology.api.constants` for
  details.

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

__all__: list[str] = []

if TYPE_CHECKING:
    from cosmology.api._constants import CosmologyConstantsNamespace


@runtime_checkable
class CosmologyNamespace(Protocol):
    """Runtime-checkable Protocol for the Cosmology API namespace."""

    @property
    def constants(self) -> CosmologyConstantsNamespace:
        """The cosmology constants API."""
        ...
