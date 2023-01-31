"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT
from cosmology.api.background import (
    BACKGROUNDCOSMO_ATTRIBUTES,
    BACKGROUNDCOSMO_METHODS,
    BackgroundCosmologyAPI,
)
from cosmology.api.components import (
    ContainsBaryons,
    ContainsColdDarkMatter,
    ContainsDarkEnergy,
    ContainsGlobalCurvature,
    ContainsMatter,
    ContainsNeutrinos,
    ContainsPhotons,
)

__all__: list[str] = []


STANDARDCOSMO_ATTRIBUTES = (
    BACKGROUNDCOSMO_ATTRIBUTES
    | frozenset(  # TODO: public scope this
        (
            "H0",
            "h",
            "hubble_distance",
            "hubble_time",
            "Om0",
            "Ode0",
            "Ok0",
            "Ob0",
            "Odm0",
            "Ogamma0",
            "Onu0",
            "Tcmb0",
            "Neff",
            "m_nu",
        ),
    )
)
STANDARDCOSMO_METHODS = BACKGROUNDCOSMO_METHODS | frozenset(  # TODO: public scope this
    (
        "H",
        "efunc",
        "inv_efunc",
        "Tcmb",
        "Om",
        "Ob",
        "Odm",
        "Ode",
        "Ogamma",
        "Onu",
        "Ok",
    ),
)


@runtime_checkable
class StandardCosmologyAPI(
    ContainsNeutrinos[ArrayT],
    ContainsBaryons[ArrayT],
    ContainsPhotons[ArrayT],
    ContainsColdDarkMatter[ArrayT],
    ContainsMatter[ArrayT],
    ContainsDarkEnergy[ArrayT],
    ContainsGlobalCurvature[ArrayT],
    BackgroundCosmologyAPI[ArrayT],
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
    # Hubble

    @property
    def H0(self) -> ArrayT:
        """Hubble function at redshift 0 in km s-1 Mpc-1."""
        ...

    @property
    def h(self) -> ArrayT:
        r"""Dimensionless Hubble parameter, h = H_0 / (100 [km/sec/Mpc])."""
        ...

    @property
    def hubble_distance(self) -> ArrayT:
        """Hubble distance in Mpc."""
        ...

    @property
    def hubble_time(self) -> ArrayT:
        """Hubble time in Gyr."""
        ...

    # ----------------------------------------------
    # Omega

    @property
    def Otot0(self) -> ArrayT:
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

    def Tcmb(self, z: ArrayT, /) -> ArrayT:
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

    # ----------------------------------------------
    # Hubble

    def H(self, z: ArrayT, /) -> ArrayT:
        """Hubble function :math:`H(z)` in km s-1 Mpc-1.

        Parameters
        ----------
        z : Array
            The redshift(s) at which to evaluate the Hubble parameter.

        Returns
        -------
        Array
        """
        ...

    def efunc(self, z: ArrayT, /) -> ArrayT:
        """Standardised Hubble function :math:`E(z) = H(z)/H_0`.

        Parameters
        ----------
        z : Array
            The redshift(s) at which to evaluate efunc.

        Returns
        -------
        Array
        """
        ...

    def inv_efunc(self, z: ArrayT, /) -> ArrayT:
        """Inverse of ``efunc``.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    # ----------------------------------------------
    # Omega

    def Otot(self, z: ArrayT, /) -> ArrayT:
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
