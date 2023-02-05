"""The Cosmology API standard for compatability wrappers."""

from cosmology.api.compat.background import BackgroundCosmologyWrapperAPI
from cosmology.api.compat.core import CosmologyWrapperAPI
from cosmology.api.compat.standard import StandardCosmologyWrapperAPI

__all__ = [
    "CosmologyWrapperAPI",
    "BackgroundCosmologyWrapperAPI",
    "StandardCosmologyWrapperAPI",
]
