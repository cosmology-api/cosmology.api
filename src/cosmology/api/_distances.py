"""The API for background calculations."""

from __future__ import annotations

from typing import Protocol, overload, runtime_checkable

from cosmology.api._array_api import Array
from cosmology.api._core import InputT

__all__: list[str] = []


@runtime_checkable
class HasTCMB0(Protocol[Array]):
    r"""The object contains a background temperature -- :math:`T_{CMB}`."""

    @property
    def T_cmb0(self) -> Array:
        """CMB temperature in K at z=0."""


@runtime_checkable
class HasTCMB(Protocol[Array, InputT]):
    r"""The object contains a background temperature method."""

    def T_cmb(self, z: InputT, /) -> Array:
        """CMB temperature in K at redshift z.

        Parameters
        ----------
        z : Array or float, positional-only
            Input redshift.

        Returns
        -------
        Array

        """


@runtime_checkable
class TemperatureCMB(
    HasTCMB[Array, InputT],
    HasTCMB0[Array],
    Protocol,
):
    r"""The object has attributes and methods for the background temperature."""


# ==============================================================================


@runtime_checkable
class HasScaleFactor0(Protocol[Array]):
    """The object contains a scale factor, described by :math:`a_0`."""

    @property
    def scale_factor0(self) -> Array:
        """Scale factor at z=0."""


@runtime_checkable
class HasScaleFactor(Protocol[Array, InputT]):
    """The object contains a scale factor method."""

    def scale_factor(self, z: InputT, /) -> Array:
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


@runtime_checkable
class ScaleFactor(
    HasScaleFactor[Array, InputT],
    HasScaleFactor0[Array],
    Protocol,
):
    """The object has attributes and methods for the scale factor."""


# ==============================================================================


@runtime_checkable
class HasComovingDistance(Protocol[Array, InputT]):
    """The object has a comoving distance method."""

    @overload
    def comoving_distance(self, z: InputT, /) -> Array: ...

    @overload
    def comoving_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def comoving_distance(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        r"""Comoving line-of-sight distance :math:`d_c` in Mpc.

        The comoving distance along the line-of-sight between two objects
        remains constant with time for objects in the Hubble flow.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d_c(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d_c(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The comoving distance :math:`d_c` in Mpc.

        """


@runtime_checkable
class HasInverseComovingDistance(Protocol[Array, InputT]):
    """The object has a inverse comoving distance method."""

    def inv_comoving_distance(self, dc: InputT, /) -> Array:
        r"""Redshift at a given comoving line-of-sight distance.

        The redshift at a comoving distance along the line-of-sight
        between two objects.

        Parameters
        ----------
        dc : Array, positional-only
            The comoving line-of-sight distance :math:`d_c` in Mpc.

        Returns
        -------
        Array
            The redshift at a given comoving line-of-sight distance.

        """


@runtime_checkable
class HasTransverseComovingDistance(Protocol[Array, InputT]):
    """The object has a comoving transverse distance method."""

    @overload
    def transverse_comoving_distance(self, z: InputT, /) -> Array: ...

    @overload
    def transverse_comoving_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def transverse_comoving_distance(
        self, z1: InputT, z2: InputT | None = None, /
    ) -> Array:
        r"""Transverse comoving distance :math:`d_M` in Mpc.

        This value is the transverse comoving distance at redshift ``z``
        corresponding to an angular separation of 1 radian. This is the same as
        the comoving distance if :math:`\Omega_k` is zero (as in the current
        concordance Lambda-CDM model).

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d_M(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d_M(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The comoving transverse distance :math:`d_M` in Mpc.

        """


@runtime_checkable
class HasComovingVolume(Protocol[Array, InputT]):
    """The object has a comoving volume method."""

    @overload
    def comoving_volume(self, z: InputT, /) -> Array: ...

    @overload
    def comoving_volume(self, z1: InputT, z2: InputT, /) -> Array: ...

    def comoving_volume(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        r"""Comoving volume :math:`V_c` in Mpc3.

        This is the volume of the universe encompassed by redshifts less than
        ``z``. For the case of :math:`\Omega_k = 0` it is a sphere of radius
        `comoving_distance` but it is less intuitive if :math:`\Omega_k` is not.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the volume
            :math:`V_c(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the volume :math:`V_c(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The comoving volume :math:`V_c` in Mpc3.

        """


@runtime_checkable
class HasDifferentialComovingVolume(Protocol[Array, InputT]):
    """The object has a differential comoving volume method."""

    def differential_comoving_volume(self, z: InputT, /) -> Array:
        r"""Differential comoving volume in Mpc3 per steradian.

        If :math:`V_c` is the comoving volume of a redshift slice with solid
        angle :math:`\Omega`, this function returns

        .. math::

            \mathtt{differential\_comoving\_volume(z)}
            = \frac{dV_c}{d\Omega \, dz}
            = \frac{c \, d_M^2(z)}{H(z)} \;.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
            The differential comoving volume :math:`dV_c` in Mpc3 sr-1.

        """


@runtime_checkable
class ComovingDistanceMeasures(
    HasComovingDistance[Array, InputT],
    HasInverseComovingDistance[Array, InputT],
    HasTransverseComovingDistance[Array, InputT],
    HasComovingVolume[Array, InputT],
    HasDifferentialComovingVolume[Array, InputT],
    Protocol,
):
    """The object has attributes and methods for comoving distance measures."""


# ============================================================================


@runtime_checkable
class HasProperDistance(Protocol[Array, InputT]):
    """The object has a proper distance method."""

    @overload
    def proper_distance(self, z: InputT, /) -> Array: ...

    @overload
    def proper_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def proper_distance(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        r"""Proper distance :math:`d` in Mpc.

        The proper distance is the distance between two objects at redshifts
        ``z1`` and ``z2``, including the effects of the expansion of the
        universe.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The proper distance :math:`d` in Mpc.

        """


@runtime_checkable
class HasProperTime(Protocol[Array, InputT]):
    """The object has a proper time method."""

    @overload
    def proper_time(self, z: InputT, /) -> Array: ...

    @overload
    def proper_time(self, z1: InputT, z2: InputT, /) -> Array: ...

    def proper_time(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        r"""Proper time :math:`t` in Gyr.

        The proper time is the proper distance divided by
        :attr:`~cosmology.api.CosmologyConstantsNamespace.c`.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the time
            :math:`t(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the time :math:`t(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The proper time :math:`t` in Gyr.

        """


@runtime_checkable
class ProperDistanceMeasures(
    HasProperDistance[Array, InputT],
    HasProperTime[Array, InputT],
    Protocol,
):
    """The object has attributes and methods for proper distance measures."""


# ============================================================================


@runtime_checkable
class HasLookbackDistance(Protocol[Array, InputT]):
    """The object has a lookback distance method."""

    @overload
    def lookback_distance(self, z: InputT, /) -> Array: ...

    @overload
    def lookback_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def lookback_distance(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        r"""Lookback distance :math:`d_T` in Mpc.

        The lookback distance is the subjective distance it took light to travel
        from redshift ``z1`` to  ``z2``.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d_T(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d_T(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The lookback distance :math:`d_T` in Mpc.

        """


@runtime_checkable
class HasLookbackTime(Protocol[Array, InputT]):
    """The object has a lookback time method."""

    @overload
    def lookback_time(self, z: InputT, /) -> Array: ...

    @overload
    def lookback_time(self, z1: InputT, z2: InputT, /) -> Array: ...

    def lookback_time(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        """Lookback time in Gyr.

        The lookback time is the time that it took light from being emitted at
        one redshift to being observed at another redshift. Effectively it is the
        difference between the age of the Universe at the two redshifts.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the time
            :math:`t_T(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the time :math:`t_T(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The lookback time in Gyr.

        """


@runtime_checkable
class LookbackDistanceMeasures(
    HasLookbackDistance[Array, InputT],
    HasLookbackTime[Array, InputT],
    Protocol,
):
    """The object has attributes and methods for lookback distance measures."""


# ============================================================================


@runtime_checkable
class HasAge(Protocol[Array, InputT]):
    """The object has an age method."""

    def age(self, z: InputT, /) -> Array:
        r"""Age of the universe at redshift ``z`` in Gyr.

        Parameters
        ----------
        z : Array
            Input redshift.

        Returns
        -------
        Array

        """


@runtime_checkable
class HasAngularDiameterDistance(Protocol[Array, InputT]):
    """The object has an angular diameter distance method."""

    @overload
    def angular_diameter_distance(self, z: InputT, /) -> Array: ...

    @overload
    def angular_diameter_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def angular_diameter_distance(
        self, z1: InputT, z2: InputT | None = None, /
    ) -> Array:
        """Angular diameter distance :math:`d_A` in Mpc.

        This gives the proper (sometimes called 'physical') transverse distance
        corresponding to an angle of 1 radian for an object at redshift ``z``
        ([1]_, [2]_, [3]_).

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d_A(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d_A(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The angular diameter distance :math:`d_A` in Mpc.

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 421-424.
        .. [2] Weedman, D. (1986). Quasar astronomy, pp 65-67.
        .. [3] Peebles, P. (1993). Principles of Physical Cosmology, pp 325-327.

        """


@runtime_checkable
class HasLuminosityDistance(Protocol[Array, InputT]):
    """The object has a luminosity distance method."""

    @overload
    def luminosity_distance(self, z: InputT, /) -> Array: ...

    @overload
    def luminosity_distance(self, z1: InputT, z2: InputT, /) -> Array: ...

    def luminosity_distance(self, z1: InputT, z2: InputT | None = None, /) -> Array:
        """Redshift-dependent luminosity distance :math:`d_L` in Mpc.

        This is the distance to use when converting between the bolometric flux
        from an object at redshift ``z`` and its bolometric luminosity [1]_.

        Parameters
        ----------
        z : Array, positional-only
        z1, z2 : Array, positional-only
            Input redshifts. If one argument ``z`` is given, the distance
            :math:`d_L(0, z)` is returned. If two arguments ``z1, z2`` are
            given, the distance :math:`d_L(z_1, z_2)` is returned.

        Returns
        -------
        Array
            The luminosity distance :math:`d_L` in Mpc.

        References
        ----------
        .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 60-62.

        """


##############################################################################
# Total


@runtime_checkable
class DistanceMeasures(
    ScaleFactor[Array, InputT],
    TemperatureCMB[Array, InputT],
    ComovingDistanceMeasures[Array, InputT],
    ProperDistanceMeasures[Array, InputT],
    LookbackDistanceMeasures[Array, InputT],
    HasAge[Array, InputT],
    HasAngularDiameterDistance[Array, InputT],
    HasLuminosityDistance[Array, InputT],
    Protocol,
):
    """Cosmology API protocol for isotropic cosmologies.

    This is a protocol class that defines the standard API for isotropic
    background calculations. It is not intended to be instantiated. Instead, it
    should be used for ``isinstance`` checks or as an ABC for libraries that
    wish to define a compatible cosmology class.
    """
