"""The Cosmology API standard for compatability wrappers."""

# LOCAL
from cosmology.api.compat.core import CosmologyWrapperAPI
from cosmology.api.compat.flrw import FLRWCosmologyWrapperAPI
from cosmology.api.compat.flrwstandard import StandardFLRWCosmologyWrapperAPI

__all__ = [
    "CosmologyWrapperAPI",
    "FLRWCosmologyWrapperAPI",
    "StandardFLRWCosmologyWrapperAPI",
]
