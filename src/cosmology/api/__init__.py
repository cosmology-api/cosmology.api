"""The Cosmology API standard."""

# LOCAL
from cosmology.api.background import BackgroundCosmologyAPI
from cosmology.api.compat import (
    BackgroundCosmologyWrapperAPI,
    CosmologyWrapperAPI,
    StandardCosmologyWrapperAPI,
)
from cosmology.api.constants import CosmologyConstantsAPINamespace
from cosmology.api.core import CosmologyAPI
from cosmology.api.namespace import CosmologyAPINamespace
from cosmology.api.standard import StandardCosmologyAPI

__all__ = [
    "CosmologyAPI",
    "BackgroundCosmologyAPI",
    "StandardCosmologyAPI",
    # wrappers
    "CosmologyWrapperAPI",
    "BackgroundCosmologyWrapperAPI",
    "StandardCosmologyWrapperAPI",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
