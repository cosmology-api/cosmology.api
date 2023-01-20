"""The Cosmology API."""

from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Protocol, runtime_checkable

# LOCAL
from cosmology.api.flrw import FLRW_ATTRIBUTES, FLRW_METHODS, FLRWCosmologyAPI

if TYPE_CHECKING:
    # LOCAL
    from ._array_api.array import Array

__all__: list[str] = []


STANDARDFLRW_ATTRIBUTES = FLRW_ATTRIBUTES | frozenset(  # TODO: public scope this
    (
        "Om0",
        "Ode0",
        "Tcmb0",
        "Neff",
        "m_nu",
        "Ob0",
        "Odm0",
        "Ogamma0",
        "Onu0",
        "rho_m0",
        "rho_b0",
        "rho_dm0",
        "rho_de0",
        "rho_gamma0",
        "rho_nu0",
    )
)
STANDARDFLRW_METHODS = FLRW_METHODS | frozenset(  # TODO: public scope this
    (
        "Tcmb",
        "Om",
        "Ob",
        "Odm",
        "Ode",
        "Ogamma",
        "Onu",
        "rho_m",
        "rho_de",
        "rho_b",
        "rho_dm",
        "rho_gamma",
        "rho_nu",
    )
)


@runtime_checkable
class StandardFLRWCosmologyAPI(FLRWCosmologyAPI, Protocol):
    """API Protocol for FLRW-like cosmologies with the standard set of components.

    This is a protocol class that defines the standard API for FLRW-like
    cosmologies. It is not intended to be instantiaed. Instead, it should be
    used for ``isinstance`` checks or as an ABC for libraries that wish to
    define a compatible cosmology class.
    """

    @property
    def Tcmb0(self) -> Array:
        """Temperature of the CMB at redshift 0 in Kelvin."""
        ...

    # ----------------------------------------------
    # Omega

    @property
    def Otot0(self) -> Array:
        r"""Omega total; the total density/critical density at z=0.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Returns
        -------
        Array
        """
        ...

    @property
    def Om0(self) -> Array:
        """Omega matter; matter density/critical density at z=0."""
        ...

    @property
    def Odm0(self) -> Array:
        """Omega dark matter; dark matter density/critical density at z=0."""
        ...

    @property
    def Ob0(self) -> Array | None:
        """Omega baryon; baryon density/critical density at z=0."""
        ...

    @property
    def Ode0(self) -> Array:
        """Omega dark energy; dark energy density/critical density at z=0."""
        ...

    @property
    def Ogamma0(self) -> Array:
        """Omega gamma; the density/critical density of photons at z=0."""
        ...

    @property
    def Onu0(self) -> Array:
        """Omega nu; the density/critical density of neutrinos at z=0."""
        ...

    # ----------------------------------------------
    # Neutrinos

    @property
    def Neff(self) -> Array:
        """Effective number of neutrino species."""
        ...

    @property
    def m_nu(self) -> tuple[Array, ...]:
        """Neutrino mass in eV."""
        ...

    # ----------------------------------------------
    # Density

    @property
    def rho_m0(self) -> Array:
        """Matter density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_de0(self) -> Array:
        """Dark energy density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_b0(self) -> Array:
        """Baryon density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_dm0(self) -> Array:
        """Dark matter density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_gamma0(self) -> Array:
        """Radiation density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_nu0(self) -> Array:
        """Neutrino density at z = 0 in Msol Mpc-3."""
        ...

    # ==============================================================
    # Methods

    def Tcmb(self, z: Array, /) -> Array:
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
    # Omega

    def Otot(self, z: Array, /) -> Array:
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

    def Om(self, z: Array, /) -> Array:
        """Redshift-dependent non-relativistic matter density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest; see `Onu`.
        """
        ...

    def Ob(self, z: Array, /) -> Array:
        """Redshift-dependent baryon density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array

        Raises
        ------
        ValueError
            If ``Ob0`` is `None`.
        """
        ...

    def Odm(self, z: Array, /) -> Array:
        """Redshift-dependent dark matter density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array

        Raises
        ------
        ValueError
            If ``Ob0`` is `None`.

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest.
        """
        ...

    def Ode(self, z: Array, /) -> Array:
        """Redshift-dependent dark energy density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def Ogamma(self, z: Array, /) -> Array:
        """Redshift-dependent photon density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def Onu(self, z: Array, /) -> Array:
        r"""Redshift-dependent neutrino density parameter.

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
    # Rho

    def rho_m(self, z: Array, /) -> Array:
        """Redshift-dependent matter density in Msol Mpc-3."""
        ...

    def rho_de(self, z: Array, /) -> Array:
        """Redshift-dependent dark energy density in Msol Mpc-3."""
        ...

    def rho_gamma(self, z: Array, /) -> Array:
        """Redshift-dependent photon density in Msol Mpc-3."""
        ...

    def rho_nu(self, z: Array, /) -> Array:
        """Redshift-dependent neutrino density in Msol Mpc-3."""
        ...

    def rho_b(self, z: Array, /) -> Array:
        """Redshift-dependent baryon density in Msol Mpc-3."""
        ...

    def rho_dm(self, z: Array, /) -> Array:
        """Redshift-dependent dark matter density in Msol Mpc-3."""
        ...
