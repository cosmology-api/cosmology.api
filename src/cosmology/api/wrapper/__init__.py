"""The API standard for cosmology wrappers."""

from cosmology.api.wrapper._core import CosmologyWrapper
from cosmology.api.wrapper._standard import StandardCosmologyWrapper

__all__ = [
    "CosmologyWrapper",
    "StandardCosmologyWrapper",
]
