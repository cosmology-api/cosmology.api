"""The Cosmology API standard."""

from cosmology.api._components import (
    BaryonComponent,
    CurvatureComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    HasMNu,
    HasNeff,
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
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
    TotalComponent,
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
    "TotalComponent",
    # curvature
    "HasOmegaK0",
    "HasOmegaK",
    "CurvatureComponent",
    # matter
    "HasOmegaM0",
    "HasOmegaM",
    "MatterComponent",
    # baryons
    "HasOmegaB0",
    "HasOmegaB",
    "BaryonComponent",
    # neutrinos
    "HasOmegaNu0",
    "HasOmegaNu",
    "HasNeff",
    "HasMNu",
    "NeutrinoComponent",
    # dark energy
    "HasOmegaDE0",
    "HasOmegaDE",
    "DarkEnergyComponent",
    # dark matter
    "HasOmegaDM0",
    "HasOmegaDM",
    "DarkMatterComponent",
    # photons
    "HasOmegaGamma0",
    "HasOmegaGamma",
    "PhotonComponent",
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
