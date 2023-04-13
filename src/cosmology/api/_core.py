"""The Cosmology API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, TypeVar, runtime_checkable

from cosmology.api._array_api import ArrayT_co

if TYPE_CHECKING:
    from ._namespace import CosmologyNamespace

# The inputs types will have defaults if https://peps.python.org/pep-0696/
# is accepted.
InputT = TypeVar("InputT")  # -> TypeVar("InputT", default=ArrayT_co | float)
InputT_contra = TypeVar("InputT_contra", contravariant=True)

__all__: list[str] = []


@runtime_checkable
class Cosmology(Protocol[ArrayT_co, InputT_contra]):  # type: ignore[misc]
    """Cosmology API Protocol."""

    @property
    def __cosmology_namespace__(self) -> CosmologyNamespace:
        """Returns an object that has all the cosmology API functions on it.

        Returns
        -------
        `CosmologyNamespace`
            an object representing the cosmology API namespace. It should have
            every top-level function defined in the specification as an
            attribute. It may contain other public names as well, but it is
            recommended to only include those names that are part of the
            specification.
        """
        ...

    @property
    def name(self) -> str | None:
        """The name of the cosmology instance."""
        ...
