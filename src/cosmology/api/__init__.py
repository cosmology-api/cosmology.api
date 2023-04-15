"""The Cosmology API standard."""

from cosmology.api._components import (
    HasBaryonComponent,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasGlobalCurvatureComponent,
    HasMatterComponent,
    HasMNu,
    HasNeff,
    HasNeutrinoComponent,
    HasOmegaB,
    HasOmegaB0,
    HasOmegaDE,
    HasOmegaDE0,
    HasOmegaDM,
    HasOmegaDM0,
    HasOmegaGamma,
    HasOmegaGamma0,
    HasOmegaK,
    HasOmegaK0,
    HasOmegaM,
    HasOmegaM0,
    HasOmegaNu,
    HasOmegaNu0,
    HasOmegaTot,
    HasOmegaTot0,
    HasPhotonComponent,
    HasTotalComponent,
)
from cosmology.api._constants import CosmologyConstantsNamespace
from cosmology.api._core import Cosmology
from cosmology.api._distances import (
    HasBackgroundTemperature,
    HasDistanceMeasures,
    HasScaleFactor,
    HasScaleFactor0,
    HasScaleFactorDistance,
    HasTcmb,
    HasTcmb0,
)
from cosmology.api._extras import (
    HasCriticalDensity,
    HasCriticalDensity0,
    HasCriticalDensityMethods,
    HasH,
    HasH0,
    HasHubbleDistance,
    HasHubbleMethods,
    HasHubbleTime,
)
from cosmology.api._namespace import CosmologyNamespace
from cosmology.api._standard import StandardCosmology
from cosmology.api.compat import (
    CosmologyWrapper,
    StandardCosmologyWrapper,
)

__all__ = [
    "Cosmology",
    "StandardCosmology",
    # --- Components ---
    # total
    "HasOmegaTot",
    "HasOmegaTot0",
    "HasTotalComponent",
    # curvature
    "HasOmegaK0",
    "HasOmegaK",
    "HasGlobalCurvatureComponent",
    # matter
    "HasOmegaM0",
    "HasOmegaM",
    "HasMatterComponent",
    # baryons
    "HasOmegaB0",
    "HasOmegaB",
    "HasBaryonComponent",
    # neutrinos
    "HasOmegaNu0",
    "HasOmegaNu",
    "HasNeff",
    "HasMNu",
    "HasNeutrinoComponent",
    # dark energy
    "HasOmegaDE0",
    "HasOmegaDE",
    "HasDarkEnergyComponent",
    # dark matter
    "HasOmegaDM0",
    "HasOmegaDM",
    "HasDarkMatterComponent",
    # photons
    "HasOmegaGamma0",
    "HasOmegaGamma",
    "HasPhotonComponent",
    # --- Parametrizations ---
    # critical density
    "HasCriticalDensity0",
    "HasCriticalDensity",
    "HasCriticalDensityMethods",
    # hubble parameter
    "HasH0",
    "HasHubbleDistance",
    "HasHubbleTime",
    "HasH",
    "HasHubbleMethods",
    # --- Distances ---
    "HasDistanceMeasures",
    # scale factor
    "HasScaleFactor",
    "HasScaleFactor0",
    "HasScaleFactorDistance",
    # background temperature
    "HasTcmb0",
    "HasTcmb",
    "HasBackgroundTemperature",
    # -- Wrappers --
    "CosmologyWrapper",
    "StandardCosmologyWrapper",
    # -- Namespaces ---
    "CosmologyNamespace",
    "CosmologyConstantsNamespace",
]
