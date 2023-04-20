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
    DistanceMeasures,
    HasAge,
    HasAngularDiameterDistance,
    HasComovingDistance,
    HasComovingTransverseDistance,
    HasComovingVolume,
    HasDifferentialComovingVolume,
    HasLookbackTime,
    HasLuminosityDistance,
    HasScaleFactor,
    HasScaleFactor0,
    HasTCMB,
    HasTCMB0,
    ScaleFactor,
    TemperatureCMB,
)
from cosmology.api._extras import (
    CriticalDensity,
    HasCriticalDensity,
    HasCriticalDensity0,
    HasH,
    HasH0,
    HasHoverH0,
    HasHubbleDistance,
    HasHubbleTime,
    HubbleParameter,
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
    "CriticalDensity",
    # hubble parameter
    "HasH0",
    "HasHubbleDistance",
    "HasHubbleTime",
    "HasH",
    "HasHoverH0",
    "HubbleParameter",
    # --- Distances ---
    "DistanceMeasures",
    # scale factor
    "HasScaleFactor",
    "HasScaleFactor0",
    "ScaleFactor",
    # background temperature
    "HasTCMB0",
    "HasTCMB",
    "TemperatureCMB",
    # distance
    "HasComovingDistance",
    "HasComovingTransverseDistance",
    "HasComovingVolume",
    "HasDifferentialComovingVolume",
    "HasLuminosityDistance",
    "HasAngularDiameterDistance",
    # time
    "HasAge",
    "HasLookbackTime",
    # -- Wrappers --
    "CosmologyWrapper",
    "StandardCosmologyWrapper",
    # -- Namespaces ---
    "CosmologyNamespace",
    "CosmologyConstantsNamespace",
]
