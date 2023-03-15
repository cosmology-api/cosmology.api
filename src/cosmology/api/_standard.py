"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT_co
from cosmology.api._components import (
    HasBaryonComponent,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasGlobalCurvatureComponent,
    HasMatterComponent,
    HasNeutrinoComponent,
    HasPhotonComponent,
    HasTotalComponent,
)
from cosmology.api._core import Cosmology, InputT_contra
from cosmology.api._distances import HasDistanceMeasures
from cosmology.api._extras import HasCriticalDensity, HasHubbleParameter

__all__: list[str] = []


@runtime_checkable
class StandardCosmology(
    HasNeutrinoComponent[ArrayT_co, InputT_contra],
    HasBaryonComponent[ArrayT_co, InputT_contra],
    HasPhotonComponent[ArrayT_co, InputT_contra],
    HasDarkMatterComponent[ArrayT_co, InputT_contra],
    HasMatterComponent[ArrayT_co, InputT_contra],
    HasDarkEnergyComponent[ArrayT_co, InputT_contra],
    HasGlobalCurvatureComponent[ArrayT_co, InputT_contra],
    HasTotalComponent[ArrayT_co, InputT_contra],
    HasHubbleParameter[ArrayT_co, InputT_contra],
    HasCriticalDensity[ArrayT_co, InputT_contra],
    HasDistanceMeasures[ArrayT_co, InputT_contra],
    Cosmology[ArrayT_co, InputT_contra],
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
    def Omega_tot0(self) -> ArrayT_co:
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
    def Omega_tot(self, z: InputT_contra, /) -> ArrayT_co:
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
