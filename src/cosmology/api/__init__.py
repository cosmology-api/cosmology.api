"""The Cosmology API standard."""

from cosmology.api import compat, component
from cosmology.api._constants import CosmologyConstantsNamespace
from cosmology.api._core import Cosmology
from cosmology.api._distances import HasDistanceMeasures
from cosmology.api._extras import HasCriticalDensity, HasHubbleParameter
from cosmology.api._namespace import CosmologyNamespace
from cosmology.api._standard import StandardCosmology
from cosmology.api.compat import (
    CosmologyWrapper,
    StandardCosmologyWrapper,
)

__all__ = [
    # Modules
    "compat",
    "component",
    # Classes
    "Cosmology",
    "HasDistanceMeasures",
    "StandardCosmology",
    # parametrizations
    "HasCriticalDensity",
    "HasHubbleParameter",
    # wrappers
    "CosmologyWrapper",
    "StandardCosmologyWrapper",
    # Namespaces
    "CosmologyNamespace",
    "CosmologyConstantsNamespace",
]
