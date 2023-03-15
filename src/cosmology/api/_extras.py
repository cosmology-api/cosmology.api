"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT_co
from cosmology.api._core import Cosmology, InputT_contra

__all__: list[str] = []


class HasCriticalDensity(Cosmology[ArrayT_co, InputT_contra], Protocol):
    """The cosmology has methods for the critical density."""

    @property
    def critical_density0(self) -> ArrayT_co:
        """Critical density at z = 0 in Msol Mpc-3."""
        ...

    def critical_density(self, z: InputT_contra, /) -> ArrayT_co:
        """Redshift-dependent critical density in Msol Mpc-3."""
        ...


class HasHubbleParameter(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology has methods to retrieve the Hubble parameter :math:`H`."""

    @property
    def H0(self) -> ArrayT_co:
        """Hubble parameter at redshift 0 in km s-1 Mpc-1."""
        ...

    @property
    def hubble_distance(self) -> ArrayT_co:
        """Hubble distance in Mpc."""
        ...

    @property
    def hubble_time(self) -> ArrayT_co:
        """Hubble time in Gyr."""
        ...

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
            The redshift(s) at which to evaluate.

        Returns
        -------
        Array
        """
        ...
