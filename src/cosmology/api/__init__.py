"""The Cosmology API standard."""

# LOCAL
from cosmology.api.compat import CosmologyAPIConformantWrapper, FLRWAPIConformantWrapper
from cosmology.api.constants import CosmologyConstantsAPINamespace
from cosmology.api.core import CosmologyAPIConformant
from cosmology.api.flrw import FLRWAPIConformant
from cosmology.api.namespace import CosmologyAPINamespace

__all__ = [
    "CosmologyAPIConformant",
    "FLRWAPIConformant",
    # wrappers
    "CosmologyAPIConformantWrapper",
    "FLRWAPIConformantWrapper",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
