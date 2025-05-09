"""The cosmology API."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import Array
from cosmology.api._core import InputT

__all__: list[str] = []

# ============================================================================


@runtime_checkable
class HasCriticalDensity0(Protocol[Array]):
    r"""The object has a critical density attribute -- :math:`\rho_{\rm crit}`."""

    @property
    def critical_density0(self) -> Array:
        """Critical density at z = 0 in Msol Mpc-3."""


@runtime_checkable
class HasCriticalDensity(Protocol[Array, InputT]):
    """The object has a critical density method."""

    def critical_density(self, z: InputT, /) -> Array:
        """Redshift-dependent critical density in Msol Mpc-3."""


@runtime_checkable
class CriticalDensity(
    HasCriticalDensity[Array, InputT],
    HasCriticalDensity0[Array],
    Protocol,
):
    """The object has attributes and methods for the critical density."""


# ============================================================================


@runtime_checkable
class HasLittleH(Protocol[Array]):
    r"""The object has a "little h" Hubble parameter attribute :math:`h`."""

    @property
    def h(self) -> Array:
        """Hubble parameter :math:`h` today."""


@runtime_checkable
class HasH0(Protocol[Array]):
    r"""The object has a Hubble parameter attribute -- :math:`H_0`."""

    @property
    def H0(self) -> Array:
        """Hubble parameter at redshift 0 in km s-1 Mpc-1."""


@runtime_checkable
class HasHubbleDistance(Protocol[Array]):
    r"""The object has a Hubble distance attribute."""

    @property
    def hubble_distance(self) -> Array:
        """Hubble distance in Mpc."""


@runtime_checkable
class HasHubbleTime(Protocol[Array]):
    r"""The object has a Hubble time attribute."""

    @property
    def hubble_time(self) -> Array:
        """Hubble time in Gyr."""


@runtime_checkable
class HasH(Protocol[Array, InputT]):
    r"""The object has a Hubble parameter method -- :math:`H(z)`."""

    def H(self, z: InputT, /) -> Array:
        """Hubble parameter :math:`H(z)` in km s-1 Mpc-1.

        Parameters
        ----------
        z : Array
            The redshift(s) at which to evaluate the Hubble parameter.

        Returns
        -------
        Array

        """


@runtime_checkable
class HasHoverH0(Protocol[Array, InputT]):
    r"""The object has a standardized Hubble parameter method -- :math:`E(z)`."""

    def H_over_H0(self, z: InputT, /) -> Array:
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


@runtime_checkable
class HubbleParameter(
    HasHoverH0[Array, InputT],
    HasH[Array, InputT],
    HasHubbleDistance[Array],
    HasHubbleTime[Array],
    HasH0[Array],
    Protocol,
):
    r"""The object has methods for working with hubble quantities."""
