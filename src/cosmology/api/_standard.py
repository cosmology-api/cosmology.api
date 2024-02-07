"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import Array
from cosmology.api._components import (
    BaryonComponent,
    CurvatureComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
    TotalComponent,
)
from cosmology.api._core import Cosmology, InputT
from cosmology.api._distances import DistanceMeasures
from cosmology.api._extras import CriticalDensity, HubbleParameter

__all__: list[str] = []


@runtime_checkable
class StandardCosmology(
    NeutrinoComponent[Array, InputT],
    BaryonComponent[Array, InputT],
    PhotonComponent[Array, InputT],
    DarkMatterComponent[Array, InputT],
    MatterComponent[Array, InputT],
    DarkEnergyComponent[Array, InputT],
    CurvatureComponent[Array, InputT],
    TotalComponent[Array, InputT],
    HubbleParameter[Array, InputT],
    CriticalDensity[Array, InputT],
    DistanceMeasures[Array, InputT],
    Cosmology[Array, InputT],
    Protocol,
):
    """API Protocol for the standard cosmology and expected set of components.

    This is a protocol class that defines the standard API for the standard
    (FLRW-like) cosmology cosmology. It is not intended to be instantiaed.
    Instead, it should be used for ``isinstance`` checks or as an ABC for
    libraries that wish to define a compatible cosmology class.
    """

    # Override from the base classes, for better docstring.
    @property
    def Omega_tot0(self) -> Array:
        r"""Omega total; the total density/critical density at z=0.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Returns
        -------
        Array

        """
        ...

    # Override from the base classes, for better docstring.
    def Omega_tot(self, z: InputT, /) -> Array:
        r"""Redshift-dependent total density parameter.

        This is the sum of the matter, radiation, neutrino, dark energy, and
        curvature density parameters.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """
        ...
