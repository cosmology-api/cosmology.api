"""The Cosmology API."""

from __future__ import annotations

__all__ = [
    "Array",
    "Cosmology",
    "InputT",
]

from typing import TYPE_CHECKING, Protocol, TypeVar, runtime_checkable

from typing_protocol_intersection import ProtocolIntersection as Cosmology

from cosmology.api._array_api import Array

if TYPE_CHECKING:
    from cosmology.api._constants import CosmologyConstantsNamespace
    from cosmology.api._namespace import CosmologyNamespace

# The inputs types will have defaults if https://peps.python.org/pep-0696/
# is accepted.
InputT = TypeVar("InputT", contravariant=True)  # noqa: PLC0105


@runtime_checkable
class _Cosmology(Protocol[Array, InputT]):  # type: ignore[misc] # noqa: PYI046
    """Cosmology API Protocol."""

    @property
    def __cosmology_namespace__(self) -> CosmologyNamespace:
        """The cosmology namespace for this cosmology object."""

    @property
    def name(self) -> str | None:
        """The name of the cosmology instance.

        This is a human-friendly label for the cosmology instance. It is
        optional, and may be `None`. If set, it should be a string. The name is
        useful for identifying the cosmology instance, for example logging the
        name in an analysis pipeline, presenting helpful error messages, and
        for plotting.
        """

    # ========================================================================
    # Convenience methods

    @property
    def constants(self) -> CosmologyConstantsNamespace:
        """The constants namespace for this cosmology object."""
        return self.__cosmology_namespace__.constants
