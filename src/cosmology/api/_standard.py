"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT
from cosmology.api._components import (
    HasBaryonComponent,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasGlobalCurvatureComponent,
    HasMatterComponent,
    HasNeutrinoComponent,
    HasPhotonComponent,
)
from cosmology.api._distances import HasDistanceMeasures
from cosmology.api._extras import HasHubbleParameter, HasTcmb

__all__: list[str] = []


@runtime_checkable
class StandardCosmology(
    HasNeutrinoComponent[ArrayT],
    HasBaryonComponent[ArrayT],
    HasPhotonComponent[ArrayT],
    HasDarkMatterComponent[ArrayT],
    HasMatterComponent[ArrayT],
    HasDarkEnergyComponent[ArrayT],
    HasGlobalCurvatureComponent[ArrayT],
    HasTcmb[ArrayT],
    HasHubbleParameter[ArrayT],
    HasDistanceMeasures[ArrayT],
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

    # Override from the base classes, for better docstring.
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
