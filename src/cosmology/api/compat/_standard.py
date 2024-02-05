"""The Cosmology API standard."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import Array
from cosmology.api._core import InputT
from cosmology.api._standard import StandardCosmology
from cosmology.api.compat._core import CosmologyWrapper

__all__: list[str] = []


class StandardCosmologyWrapper(
    CosmologyWrapper[Array, InputT],
    StandardCosmology[Array, InputT],
    Protocol,
):
    """The standard for ``StandardCosmology`` compatability wrappers.

    This is a protocol class that defines an API standard. It is not intended to
    be used directly, and should not be instantiated. Instead, it should be used
    as a Protocol or ABC for libraries that wish to define a wrapper for the
    standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.

    """
