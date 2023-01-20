"""The Cosmology API."""

from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:

    # LOCAL
    from .namespace import CosmologyAPINamespace

__all__: list[str] = []


@runtime_checkable
class CosmologyAPI(Protocol):
    """Cosmology API Protocol."""

    def __cosmology_namespace__(
        self, /, *, api_version: str | None = None
    ) -> CosmologyAPINamespace:
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
        `CosmologyAPINamespace`
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
