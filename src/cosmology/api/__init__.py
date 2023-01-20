"""The Cosmology API standard."""

# LOCAL
from cosmology.api.compat import CosmologyWrapperAPI, FLRWCosmologyWrapperAPI
from cosmology.api.constants import CosmologyConstantsAPINamespace
from cosmology.api.core import CosmologyAPI
from cosmology.api.flrw import FLRWCosmologyAPI
from cosmology.api.namespace import CosmologyAPINamespace

__all__ = [
    "CosmologyAPI",
    "FLRWCosmologyAPI",
    # wrappers
    "CosmologyWrapperAPI",
    "FLRWCosmologyWrapperAPI",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
