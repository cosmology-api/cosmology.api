"""The Cosmology API standard."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api.background import BackgroundCosmologyAPI
from cosmology.api.compat.core import CosmologyWrapperAPI

__all__: list[str] = []


class BackgroundCosmologyWrapperAPI(
    CosmologyWrapperAPI[ArrayT], BackgroundCosmologyAPI[ArrayT], Protocol
):
    """The Cosmology API standard for FLRW compatability wrappers.

    This is a protocol class that defines the standard API for FLRW classes. It
    is not intended to be used directly, and should not be instantiated.
    Instead, it should be used as a Protocol or ABC for libraries that wish to
    define a wrapper for the standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.

    See Also
    --------
    cosmology.api.compat.core.StandardCosmologyWrapperAPI
        The FLRW Cosmology wrapper API, with the standard set of components:
        matter, radiation, dark energy, dark matter, neutrinos.
    """
