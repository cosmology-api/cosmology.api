"""The Cosmology API standard for compatability wrappers."""

from cosmology.api.compat._core import CosmologyWrapperAPI
from cosmology.api.compat._standard import StandardCosmologyWrapperAPI

__all__ = [
    "CosmologyWrapperAPI",
    "StandardCosmologyWrapperAPI",
]
