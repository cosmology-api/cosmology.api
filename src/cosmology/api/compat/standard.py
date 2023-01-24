"""The Cosmology API standard."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api.compat.background import BackgroundCosmologyWrapperAPI
from cosmology.api.standard import StandardCosmologyAPI

__all__: list[str] = []


class StandardCosmologyWrapperAPI(
    BackgroundCosmologyWrapperAPI[ArrayT], StandardCosmologyAPI[ArrayT], Protocol,
):
    """The standard for ``StandardCosmologyAPI`` compatability wrappers.

    This is a protocol class that defines an API standard. It is not intended to
    be used directly, and should not be instantiated. Instead, it should be used
    as a Protocol or ABC for libraries that wish to define a wrapper for the
    standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.
    """
