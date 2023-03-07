"""The API for background calculations."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT
from cosmology.api.core import CosmologyAPI

__all__: list[str] = []


@runtime_checkable
class FriedmannLemaitreRobertsonWalker(CosmologyAPI[ArrayT], Protocol):
    """Cosmology API protocol for isotropic cosmologies.

    This is a protocol class that defines the standard API for isotropic
    background calculations. It is not intended to be instantiated. Instead, it
    should be used for ``isinstance`` checks or as an ABC for libraries that
    wish to define a compatible cosmology class.

    See Also
    --------
    StandardCosmologyAPI
        The standard cosmology API, with the expected set of components: matter,
        radiation, neutrinos, dark matter, and dark energy.
    """

    @property
    def scale_factor0(self) -> ArrayT:
        """Scale factor at z=0."""
        ...

    @property
    def Otot0(self) -> ArrayT:
        r"""Omega total; the total density/critical density at z=0."""
        ...

    @property
    def critical_density0(self) -> ArrayT:
        """Critical density at z = 0 in Msol Mpc-3."""
        ...

    # ==============================================================
    # Methods

    def scale_factor(self, z: ArrayT | float, /) -> ArrayT:
        """Redshift-dependenct scale factor.

        The scale factor is defined as :math:`a = a_0 / (1 + z)`.

        Parameters
        ----------
        z : Array or float, positional-only
            The redshift(s) at which to evaluate the scale factor.

        Returns
        -------
        Array
        """
        ...

    def Otot(self, z: ArrayT | float, /) -> ArrayT:
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

    def critical_density(self, z: ArrayT | float, /) -> ArrayT:
        """Redshift-dependent critical density in Msol Mpc-3."""
        ...

    # ----------------------------------------------
    # Time

    def age(self, z: ArrayT | float, /) -> ArrayT:
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

    def lookback_time(self, z: ArrayT | float, /) -> ArrayT:
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

    def comoving_distance(self, z: ArrayT | float, /) -> ArrayT:
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

    def comoving_transverse_distance(self, z: ArrayT | float, /) -> ArrayT:
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

    def comoving_volume(self, z: ArrayT | float, /) -> ArrayT:
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

    def differential_comoving_volume(self, z: ArrayT | float, /) -> ArrayT:
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

    def angular_diameter_distance(self, z: ArrayT | float, /) -> ArrayT:
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

    def luminosity_distance(self, z: ArrayT | float, /) -> ArrayT:
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
