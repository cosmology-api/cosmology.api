"""The Cosmology API standard."""

from __future__ import annotations

# STDLIB
from typing import Protocol

# LOCAL
from cosmology.api.compat.flrw import FLRWCosmologyWrapperAPI
from cosmology.api.flrwstandard import StandardFLRWCosmologyAPI

__all__: list[str] = []


class StandardFLRWCosmologyWrapperAPI(
    FLRWCosmologyWrapperAPI, StandardFLRWCosmologyAPI, Protocol
):
    """The Cosmology API standard for FLRW compatability wrappers.

    This is a protocol class that defines the standard API for FLRW
    classes. It is not intended to be used directly, and should not be
    instantiated. Instead, it should be used as a Protocol or ABC for libraries
    that wish to define a wrapper for the standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.
    """
