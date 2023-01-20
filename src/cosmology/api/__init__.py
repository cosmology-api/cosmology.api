"""The Cosmology API standard."""

# LOCAL
from cosmology.api.compat import CosmologyWrapper, FLRWCosmologyWrapper
from cosmology.api.constants import CosmologyConstantsAPINamespace
from cosmology.api.core import CosmologyAPI
from cosmology.api.flrw import FLRWCosmologyAPI
from cosmology.api.namespace import CosmologyAPINamespace

__all__ = [
    "CosmologyAPI",
    "FLRWCosmologyAPI",
    # wrappers
    "CosmologyWrapper",
    "FLRWCosmologyWrapper",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
