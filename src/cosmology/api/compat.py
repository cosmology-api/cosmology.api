"""The Cosmology API standard."""

from __future__ import annotations

# STDLIB
from typing import Protocol

# LOCAL
from .core import CosmologyAPIConformant

__all__: list[str] = []


class CosmologyAPIConformantWrapper(CosmologyAPIConformant, Protocol):
    """The Cosmology API standard for compatability wrappers.

    This is a protocol class that defines the standard API for Cosmology
    classes. It is not intended to be used directly, and should not be
    instantiated. Instead, it should be used as a Protocol or ABC for libraries
    that wish to define a wrapper for the standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.
    """

    cosmo: object

    def __getattr__(self, name: str) -> object:
        """Pass all non Cosmology API to the wrapped object.

        Parameters
        ----------
        name: str
            The name of the attribute to get.

        Returns
        -------
        object
            The attribute of the wrapped object.
        """
        return getattr(self.cosmo, name)
