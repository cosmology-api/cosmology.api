"""The Cosmology API."""

from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Protocol, runtime_checkable

# LOCAL
from cosmology.api.core import CosmologyAPIConformant

if TYPE_CHECKING:
    # LOCAL
    from ._array_api.array import Array

__all__: list[str] = []


FLRW_ATTRIBUTES = frozenset(  # TODO: public scope this
    (
        "H0",
        "Om0",
        "Ode0",
        "Tcmb0",
        "Neff",
        "m_nu",
        "Ob0",
        "scale_factor0",
        "h",
        "hubble_distance",
        "hubble_time",
        "Otot0",
        "Odm0",
        "Ok0",
        "Ogamma0",
        "Onu0",
        "rho_critical0",
        "rho_tot0",
        "rho_m0",
        "rho_de0",
        "rho_b0",
        "rho_dm0",
        "rho_k0",
        "rho_gamma0",
        "rho_nu0",
    )
)
FLRW_METHODS = frozenset(  # TODO: public scope this
    (
        "scale_factor",
        "H",
        "efunc",
        "inv_efunc",
        "Otot",
        "Om",
        "Ob",
        "Odm",
        "Ok",
        "Ode",
        "Ogamma",
        "Onu",
        "rho_critical",
        "rho_tot",
        "rho_m",
        "rho_de",
        "rho_k",
        "rho_b",
        "rho_dm",
        "rho_gamma",
        "rho_nu",
        "age",
        "lookback_time",
        "comoving_distance",
        "comoving_transverse_distance",
        "comoving_volume",
        "differential_comoving_volume",
        "angular_diameter_distance",
        "luminosity_distance",
    )
)


@runtime_checkable
class FLRWAPIConformant(CosmologyAPIConformant, Protocol):
    """Cosmology API Protocol for FLRW-like cosmologies.

    This is a protocol class that defines the standard API for FLRW-like
    cosmologies. It is not intended to be instantiaed. Instead, it should be
    used for ``isinstance`` checks or as an ABC for libraries that wish to
    define a compatible cosmology class.
    """

    @property
    def scale_factor0(self) -> Array:
        """Scale factor at z=0."""
        ...

    @property
    def Tcmb0(self) -> Array:
        """Temperature of the CMB at redshift 0 in Kelvin."""
        ...

    # ----------------------------------------------
    # Hubble

    @property
    def H0(self) -> Array:
        """Hubble function at redshift 0 in km s-1 Mpc-1."""
        ...

    @property
    def h(self) -> Array:
        r"""Dimensionless Hubble parameter, h = H_0 / (100 [km/sec/Mpc])."""
        ...

    @property
    def hubble_distance(self) -> Array:
        """Hubble distance in Mpc."""
        ...

    @property
    def hubble_time(self) -> Array:
        """Hubble time in Gyr."""
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
    def Ok0(self) -> Array:
        """Omega curvature; the effective curvature density/critical density at z=0."""
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

    # TODO? change to rho_critical0
    @property
    def rho_critical0(self) -> Array:
        """Critical density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_tot0(self) -> Array:
        """Total density at z = 0 in Msol Mpc-3."""
        ...

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
    def rho_k0(self) -> Array:
        """Curvature density at z = 0 in Msol Mpc-3."""
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

    def scale_factor(self, z: Array, /) -> Array:
        """Redshift-dependenct scale factor.

        The scale factor is defined as :math:`a = a_0 / (1 + z)`.

        Parameters
        ----------
        z : Array, positional-only
            The redshift(s) at which to evaluate the scale factor.

        Returns
        -------
        Array
        """
        ...

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
    # Hubble

    def H(self, z: Array, /) -> Array:
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

    def efunc(self, z: Array, /) -> Array:
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

    def inv_efunc(self, z: Array, /) -> Array:
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

    def Ok(self, z: Array, /) -> Array:
        """Redshift-dependent curvature density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
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

        The energy density of neutrinos relative to the critical density at each
        redshift. Note that this includes their kinetic energy (if
        they have mass), so it is not equal to the commonly used :math:`\sum
        \frac{m_{\nu}}{94 eV}`, which does not include kinetic energy.
        Returns `float` if the input is scalar.

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

    def rho_critical(self, z: Array, /) -> Array:
        """Redshift-dependent critical density in Msol Mpc-3."""
        ...

    def rho_tot(self, z: Array, /) -> Array:
        """Redshift-dependent total density in Msol Mpc-3."""
        ...

    def rho_m(self, z: Array, /) -> Array:
        """Redshift-dependent matter density in Msol Mpc-3."""
        ...

    def rho_de(self, z: Array, /) -> Array:
        """Redshift-dependent dark energy density in Msol Mpc-3."""
        ...

    def rho_k(self, z: Array, /) -> Array:
        """Redshift-dependent curvature density in Msol Mpc-3."""
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

    # ----------------------------------------------
    # Time

    def age(self, z: Array, /) -> Array:
        """Age of the universe in Gyr at redshift ``z``.

        Parameters
        ----------
        z : Array
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def lookback_time(self, z: Array, /) -> Array:
        """Lookback time to redshift ``z`` in Gyr.

        The lookback time is the difference between the age of the Universe now
        and the age at redshift ``z``.

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
    # Comoving distance

    def comoving_distance(self, z: Array, /) -> Array:
        r"""Comoving line-of-sight distance :math:`d_c(z)` in Mpc.

        The comoving distance along the line-of-sight between two objects
        remains constant with time for objects in the Hubble flow.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def comoving_transverse_distance(self, z: Array, /) -> Array:
        r"""Transverse comoving distance :math:`d_M(z)` in Mpc.

        This value is the transverse comoving distance at redshift ``z``
        corresponding to an angular separation of 1 radian. This is the same as
        the comoving distance if :math:`\Omega_k` is zero (as in the current
        concordance Lambda-CDM model).

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def comoving_volume(self, z: Array, /) -> Array:
        r"""Comoving volume in cubic Mpc.

        This is the volume of the universe encompassed by redshifts less than
        ``z``. For the case of :math:`\Omega_k = 0` it is a sphere of radius
        `comoving_distance` but it is less intuitive if :math:`\Omega_k` is not.

        Parameters
        ----------
        z : Array
            Input redshift.

        Returns
        -------
        Array
        """
        ...

    def differential_comoving_volume(self, z: Array, /) -> Array:
        r"""Differential comoving volume in cubic Mpc per steradian.

        If :math:`V_c` is the comoving volume of a redshift slice with solid
        angle :math:`\Omega`, this function returns

        .. math::

            \mathtt{dvc(z)}
            = \frac{1}{d_H^3} \, \frac{dV_c}{d\Omega \, dz}
            = \frac{x_M^2(z)}{E(z)}
            = \frac{\mathtt{xm(z)^2}}{\mathtt{ef(z)}} \;.

        """
        ...

    # ----------------------------------------------
    # Angular diameter distance

    def angular_diameter_distance(self, z: Array, /) -> Array:
        """Angular diameter distance :math:`d_A(z)` in Mpc.

        This gives the proper (sometimes called 'physical') transverse
        distance corresponding to an angle of 1 radian for an object
        at redshift ``z`` ([1]_, [2]_, [3]_).

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 421-424.
        .. [2] Weedman, D. (1986). Quasar astronomy, pp 65-67.
        .. [3] Peebles, P. (1993). Principles of Physical Cosmology, pp 325-327.
        """
        ...

    # ----------------------------------------------
    # Luminosity distance

    def luminosity_distance(self, z: Array, /) -> Array:
        """Redshift-dependent luminosity distance in Mpc.

        This is the distance to use when converting between the bolometric flux
        from an object at redshift ``z`` and its bolometric luminosity [1]_.

        Parameters
        ----------
        z : Array
            Input redshift.

        Returns
        -------
        Array

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 60-62.
        """
        ...
