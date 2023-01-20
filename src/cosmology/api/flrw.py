"""The Cosmology API."""

from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Protocol, runtime_checkable

# LOCAL
from cosmology.api.core import CosmologyAPI

if TYPE_CHECKING:
    # LOCAL
    from ._array_api.array import Array

__all__: list[str] = []


FLRW_ATTRIBUTES = frozenset(  # TODO: public scope this
    (
        "H0",
        "scale_factor0",
        "h",
        "hubble_distance",
        "hubble_time",
        "Otot0",
        "Ok0",
        "rho_critical0",
        "rho_tot0",
        "rho_k0",
    )
)
FLRW_METHODS = frozenset(  # TODO: public scope this
    (
        "scale_factor",
        "H",
        "efunc",
        "inv_efunc",
        "Otot",
        "Ok",
        "rho_critical",
        "rho_tot",
        "rho_k",
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
class FLRWCosmologyAPI(CosmologyAPI, Protocol):
    """Cosmology API Protocol for FLRW-like cosmologies.

    This is a protocol class that defines the standard API for FLRW-like
    cosmologies. It is not intended to be instantiaed. Instead, it should be
    used for ``isinstance`` checks or as an ABC for libraries that wish to
    define a compatible cosmology class.

    See Also
    --------
    StandardFLRWCosmologyAPI
        The FLRW Cosmology API, with the standard set of components: matter,
        radiation, dark energy, dark matter, neutrinos.
    """

    @property
    def scale_factor0(self) -> Array:
        """Scale factor at z=0."""
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

        Returns
        -------
        Array
        """
        ...

    @property
    def Ok0(self) -> Array:
        """Omega curvature; the effective curvature density/critical density at z=0."""
        ...

    # ----------------------------------------------
    # Density

    @property
    def rho_critical0(self) -> Array:
        """Critical density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_tot0(self) -> Array:
        """Total density at z = 0 in Msol Mpc-3."""
        ...

    @property
    def rho_k0(self) -> Array:
        """Curvature density at z = 0 in Msol Mpc-3."""
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

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
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

    # ----------------------------------------------
    # Rho

    def rho_critical(self, z: Array, /) -> Array:
        """Redshift-dependent critical density in Msol Mpc-3."""
        ...

    def rho_tot(self, z: Array, /) -> Array:
        """Redshift-dependent total density in Msol Mpc-3."""
        ...

    def rho_k(self, z: Array, /) -> Array:
        """Redshift-dependent curvature density in Msol Mpc-3."""
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
