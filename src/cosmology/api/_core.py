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

    def __cosmology_namespace__(
        self, /, *, api_version: str | None = None
    ) -> CosmologyNamespace:
        """Returns an object that has all the cosmology API functions on it.

        Parameters
        ----------
        api_version: Optional[str]
            string representing the version of the cosmology API specification
            to be returned, in ``'YYYY.MM'`` form, for example, ``'2020.10'``.
            If it is ``None``, it should return the namespace corresponding to
            latest version of the cosmology API specification.  If the given
            version is invalid or not implemented for the given module, an error
            should be raised. Default: ``None``.

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
