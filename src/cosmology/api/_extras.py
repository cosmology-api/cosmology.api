"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api._core import CosmologyAPI

__all__: list[str] = []


class HasHubbleParameter(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology has methods to retrieve the Hubble parameter :math:`H`."""

    @property
    def H0(self) -> ArrayT:
        """Hubble parameter at redshift 0 in km s-1 Mpc-1."""
        ...

    @property
    def hubble_distance(self) -> ArrayT:
        """Hubble distance in Mpc."""
        ...

    @property
    def hubble_time(self) -> ArrayT:
        """Hubble time in Gyr."""
        ...

    def H(self, z: ArrayT | float, /) -> ArrayT:
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

    def h_over_h0(self, z: ArrayT | float, /) -> ArrayT:
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


class HasTcmb(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains a CMB temperature, described by :math:`T_{CMB}`."""

    @property
    def Tcmb0(self) -> ArrayT:
        """CMB temperature in K at z=0."""
        ...

    def Tcmb(self, z: ArrayT | float, /) -> ArrayT:
        """CMB temperature in K at redshift z.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...
