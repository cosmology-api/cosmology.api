"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT_co
from cosmology.api._core import InputT_contra

__all__: list[str] = []

# ============================================================================


class HasCriticalDensity0(Protocol[ArrayT_co]):
    r"""The object has a critical density attribute -- :math:`\rho_{\rm crit}`."""

    @property
    def critical_density0(self) -> ArrayT_co:
        """Critical density at z = 0 in Msol Mpc-3."""
        ...


class HasCriticalDensity(Protocol[ArrayT_co, InputT_contra]):
    """The object has a critical density method."""

    def critical_density(self, z: InputT_contra, /) -> ArrayT_co:
        """Redshift-dependent critical density in Msol Mpc-3."""
        ...


class CriticalDensity(
    HasCriticalDensity[ArrayT_co, InputT_contra],
    HasCriticalDensity0[ArrayT_co],
    Protocol,
):
    """The object has attributes and methods for the critical density."""


# ============================================================================


class HasH0(Protocol[ArrayT_co]):
    r"""The object has a Hubble parameter attribute -- :math:`H_0`."""

    @property
    def H0(self) -> ArrayT_co:
        """Hubble parameter at redshift 0 in km s-1 Mpc-1."""
        ...


class HasHubbleDistance(Protocol[ArrayT_co]):
    r"""The object has a Hubble distance attribute."""

    @property
    def hubble_distance(self) -> ArrayT_co:
        """Hubble distance in Mpc."""
        ...


class HasHubbleTime(Protocol[ArrayT_co]):
    r"""The object has a Hubble time attribute."""

    @property
    def hubble_time(self) -> ArrayT_co:
        """Hubble time in Gyr."""
        ...


class HasH(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a Hubble parameter method -- :math:`H(z)`."""

    def H(self, z: InputT_contra, /) -> ArrayT_co:
        """Hubble parameter :math:`H(z)` in km s-1 Mpc-1.

        Parameters
        ----------
        z : Array
            The redshift(s) at which to evaluate the Hubble parameter.

        Returns
        -------
        Array
        """  # noqa: D402
        ...

    def h_over_h0(self, z: InputT_contra, /) -> ArrayT_co:
        """Standardised Hubble function :math:`E(z) = H(z)/H_0`.

        Parameters
        ----------
        z : Array
            The redshift(s) at which to evaluate the standardised Hubble
            parameter.

        Returns
        -------
        Array
        """
        ...


class HubbleParameter(
    HasH0[ArrayT_co],
    HasHubbleDistance[ArrayT_co],
    HasHubbleTime[ArrayT_co],
    HasH[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The object has methods for working with hubble quantities."""
