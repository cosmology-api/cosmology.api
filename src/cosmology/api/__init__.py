"""The Cosmology API standard."""

# LOCAL
from .constants import CosmologyConstantsAPINamespace
from .core import CosmologyAPIConformant
from .namespace import CosmologyAPINamespace

__all__ = [
    "CosmologyAPIConformant",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
