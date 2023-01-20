"""The Cosmology API standard for compatability wrappers."""

# LOCAL
from cosmology.api.compat.core import CosmologyWrapper
from cosmology.api.compat.flrw import FLRWCosmologyWrapper

__all__ = [
    "CosmologyWrapper",
    "FLRWCosmologyWrapper",
]
