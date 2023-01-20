"""The Cosmology API standard."""

# LOCAL
from cosmology.api.compat import (
    CosmologyWrapperAPI,
    FLRWCosmologyWrapperAPI,
    StandardFLRWCosmologyWrapperAPI,
)
from cosmology.api.constants import CosmologyConstantsAPINamespace
from cosmology.api.core import CosmologyAPI
from cosmology.api.flrw import FLRWCosmologyAPI
from cosmology.api.flrwstandard import StandardFLRWCosmologyAPI
from cosmology.api.namespace import CosmologyAPINamespace

__all__ = [
    "CosmologyAPI",
    "FLRWCosmologyAPI",
    "StandardFLRWCosmologyAPI",
    # wrappers
    "CosmologyWrapperAPI",
    "FLRWCosmologyWrapperAPI",
    "StandardFLRWCosmologyWrapperAPI",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
