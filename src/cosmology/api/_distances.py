"""The API for background calculations."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT_co
from cosmology.api._core import InputT_contra

__all__: list[str] = []


@runtime_checkable
class HasTCMB0(Protocol[ArrayT_co]):
    r"""The object contains a background temperature -- :math:`T_{CMB}`."""

    @property
    def T_cmb0(self) -> ArrayT_co:
        """CMB temperature in K at z=0."""
        ...


@runtime_checkable
class HasTCMB(Protocol[ArrayT_co, InputT_contra]):
    r"""The object contains a background temperature method."""

    def T_cmb(self, z: InputT_contra, /) -> ArrayT_co:
        """CMB temperature in K at redshift z.

        Parameters
        ----------
        z : Array or float, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class TemperatureCMB(
    HasTCMB[ArrayT_co, InputT_contra],
    HasTCMB0[ArrayT_co],
    Protocol,
):
    r"""The object has attributes and methods for the background temperature."""


# ==============================================================================


@runtime_checkable
class HasScaleFactor0(Protocol[ArrayT_co]):
    """The object contains a scale factor, described by :math:`a_0`."""

    @property
    def scale_factor0(self) -> ArrayT_co:
        """Scale factor at z=0."""
        ...


@runtime_checkable
class HasScaleFactor(Protocol[ArrayT_co, InputT_contra]):
    """The object contains a scale factor method."""

    def scale_factor(self, z: InputT_contra, /) -> ArrayT_co:
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


@runtime_checkable
class ScaleFactor(
    HasScaleFactor[ArrayT_co, InputT_contra],
    HasScaleFactor0[ArrayT_co],
    Protocol,
):
    """The object has attributes and methods for the scale factor."""


##############################################################################
# Total


@runtime_checkable
class DistanceMeasures(
    ScaleFactor[ArrayT_co, InputT_contra],
    TemperatureCMB[ArrayT_co, InputT_contra],
    Protocol,
):
    """Cosmology API protocol for isotropic cosmologies.

    This is a protocol class that defines the standard API for isotropic
    background calculations. It is not intended to be instantiated. Instead, it
    should be used for ``isinstance`` checks or as an ABC for libraries that
    wish to define a compatible cosmology class.
    """

    # ----------------------------------------------
    # Time

    def age(self, z: InputT_contra, /) -> ArrayT_co:
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

    def lookback_time(self, z: InputT_contra, /) -> ArrayT_co:
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

    def comoving_distance(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        r"""Comoving line-of-sight distance :math:`d_c(z1, z2)` in Mpc.

        The comoving distance along the line-of-sight between two objects
        remains constant with time for objects in the Hubble flow.

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the distance
            :math:`d_c(0, z)` is returned, otherwise the distance :math:`d_c(z,
            zp)` is returned.

        Returns
        -------
        Array
            The comoving distance :math:`d_c(z1, z2)` in Mpc, where ``(z1, z2)``
            is (0, `z`) if `zp` is `None` else (`z`, `zp`).
        """
        ...

    def comoving_transverse_distance(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        r"""Transverse comoving distance :math:`d_M(z1, z2)` in Mpc.

        This value is the transverse comoving distance at redshift ``z``
        corresponding to an angular separation of 1 radian. This is the same as
        the comoving distance if :math:`\Omega_k` is zero (as in the current
        concordance Lambda-CDM model).

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the distance
            :math:`d_M(0, z)` is returned, otherwise the distance :math:`d_M(z,
            zp)` is returned.

        Returns
        -------
        Array
            The comoving transverse distance :math:`d_M(z1, z2)` in Mpc, where
            ``(z1, z2)`` is (0, `z`) if `zp` is `None` else (`z`, `zp`).
        """
        ...

    def comoving_volume(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        r"""Comoving volume in cubic Mpc.

        This is the volume of the universe encompassed by redshifts less than
        ``z``. For the case of :math:`\Omega_k = 0` it is a sphere of radius
        `comoving_distance` but it is less intuitive if :math:`\Omega_k` is not.

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the
            volume :math:`V_c(0, z)` is returned, otherwise the
            volume :math:`V_c(z, zp)` is returned.

        Returns
        -------
        Array
            The comoving volume :math:`V_c(z1, z2)` in Mpc, where
            ``(z1, z2)`` is (0, `z`) if `zp` is `None` else (`z`, `zp`).
        """
        ...

    def differential_comoving_volume(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        r"""Differential comoving volume in cubic Mpc per steradian.

        If :math:`V_c` is the comoving volume of a redshift slice with solid
        angle :math:`\Omega`, this function returns

        .. math::

            \mathtt{dvc(z)}
            = \frac{1}{d_H^3} \, \frac{dV_c}{d\Omega \, dz}
            = \frac{x_M^2(z)}{E(z)}
            = \frac{\mathtt{xm(z)^2}}{\mathtt{ef(z)}} \;.

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the
            differential volume :math:`dV_c(0, z)` is returned, otherwise the
            differential volume :math:`dV_c(z, zp)` is returned.

        Returns
        -------
        Array
            The differential comoving volume :math:`dV_c(z1, z2)` in Mpc,
            where ``(z1, z2)`` is (0, `z`) if `zp` is `None` else (`z`, `zp`).
        """
        ...

    # ----------------------------------------------
    # Angular diameter distance

    def angular_diameter_distance(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        """Angular diameter distance :math:`d_A(z)` in Mpc.

        This gives the proper (sometimes called 'physical') transverse distance
        corresponding to an angle of 1 radian for an object at redshift ``z``
        ([1]_, [2]_, [3]_).

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the distance
            :math:`d_A(0, z)` is returned, otherwise the distance :math:`d_A(z,
            zp)` is returned.

        Returns
        -------
        Array
            The angular diameter distance :math:`d_A(z1, z2)` in Mpc, where
            ``(z1, z2)`` is (0, `z`) if `zp` is `None` else (`z`, `zp`).

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 421-424.
        .. [2] Weedman, D. (1986). Quasar astronomy, pp 65-67.
        .. [3] Peebles, P. (1993). Principles of Physical Cosmology, pp 325-327.
        """
        ...

    # ----------------------------------------------
    # Luminosity distance

    def luminosity_distance(
        self, z: InputT_contra, zp: InputT_contra | None = None, /
    ) -> ArrayT_co:
        """Redshift-dependent luminosity distance :math:`d_L(z1, z2)` in Mpc.

        This is the distance to use when converting between the bolometric flux
        from an object at redshift ``z`` and its bolometric luminosity [1]_.

        Parameters
        ----------
        z, zp : Array, positional-only
            Input redshifts. If ``zp`` is `None` (default), then the
            distance :math:`d_L(0, z)` is returned, otherwise the
            distance :math:`d_L(z, zp)` is returned.

        Returns
        -------
        Array
            The luminosity distance :math:`d_L(z1, z2)` in Mpc, where
            ``(z1, z2)`` is (0, `z`) if `zp` is `None` else (`z`, `zp`).

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 60-62.
        """
        ...
