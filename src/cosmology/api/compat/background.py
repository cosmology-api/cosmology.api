"""The Cosmology API standard."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api.background import BackgroundCosmologyAPI
from cosmology.api.compat.core import CosmologyWrapperAPI

__all__: list[str] = []


class BackgroundCosmologyWrapperAPI(
    CosmologyWrapperAPI[ArrayT], BackgroundCosmologyAPI[ArrayT], Protocol,
):
    """The standard for ``BacgroundCosmologyAPI`` compatability wrappers.

    This is a protocol class that defines an API standard. It is not intended to
    be used directly, and should not be instantiated. Instead, it should be used
    as a Protocol or ABC for libraries that wish to define a wrapper for the
    standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.

    See Also
    --------
    cosmology.api.compat.standard.StandardCosmologyWrapperAPI
        The standard cosmology wrapper API, with the expected set of components:
        matter, radiation, neutrinos, dark matter, and dark energy.
    """
