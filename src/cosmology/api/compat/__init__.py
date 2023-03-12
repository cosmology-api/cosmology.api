"""The Cosmology API standard for compatability wrappers."""

from cosmology.api.compat._core import CosmologyWrapper
from cosmology.api.compat._standard import StandardCosmologyWrapper

__all__ = [
    "CosmologyWrapper",
    "StandardCosmologyWrapper",
]
