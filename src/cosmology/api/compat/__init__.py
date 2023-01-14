"""The Cosmology API standard for compatability wrappers."""

# LOCAL
from cosmology.api.compat.core import CosmologyAPIConformantWrapper
from cosmology.api.compat.flrw import FLRWAPIConformantWrapper

__all__ = [
    "CosmologyAPIConformantWrapper",
    "FLRWAPIConformantWrapper",
]
