"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT
from cosmology.api._background import FriedmannLemaitreRobertsonWalker
from cosmology.api._components import (
    BaryonComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    GlobalCurvatureComponent,
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
)
from cosmology.api._extras import HasHubbleParameter

__all__: list[str] = []


@runtime_checkable
class StandardCosmologyAPI(
    NeutrinoComponent[ArrayT],
    BaryonComponent[ArrayT],
    PhotonComponent[ArrayT],
    DarkMatterComponent[ArrayT],
    MatterComponent[ArrayT],
    DarkEnergyComponent[ArrayT],
    GlobalCurvatureComponent[ArrayT],
    HasHubbleParameter[ArrayT],
    FriedmannLemaitreRobertsonWalker[ArrayT],
    Protocol,
):
    """API Protocol for the standard cosmology and expected set of components.

    This is a protocol class that defines the standard API for the standard
    (FLRW-like) cosmology cosmology. It is not intended to be instantiaed.
    Instead, it should be used for ``isinstance`` checks or as an ABC for
    libraries that wish to define a compatible cosmology class.
    """

    @property
    def Tcmb0(self) -> ArrayT:
        """Temperature of the CMB at redshift 0 in Kelvin."""
        ...

    # ----------------------------------------------
    # Omega

    @property
    def Omega_tot0(self) -> ArrayT:
        r"""Omega total; the total density/critical density at z=0.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Returns
        -------
        Array
        """
        ...

    # ==============================================================
    # Methods

    def Tcmb(self, z: ArrayT | float, /) -> ArrayT:
        """Temperature of the CMB at redshift z in Kelvin.

        Parameters
        ----------
        z : Array, positional-only
            The redshift(s) at which to evaluate the CMB temperature.

        Returns
        -------
        Array
        """
        ...

    def Omega_tot(self, z: ArrayT | float, /) -> ArrayT:
        r"""Redshift-dependent total density parameter.

        This is the sum of the matter, radiation, neutrino, dark energy, and
        curvature density parameters.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...
