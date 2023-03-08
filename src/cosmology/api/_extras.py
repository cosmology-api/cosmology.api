"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api._core import CosmologyAPI

__all__: list[str] = []


class HasHubbleParameter(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains global curvature, described by :math:`Omega_K`."""

    @property
    def H0(self) -> ArrayT:
        """Hubble function at redshift 0 in km s-1 Mpc-1."""
        ...

    @property
    def h(self) -> ArrayT:
        r"""Dimensionless Hubble parameter, h = H_0 / (100 [km/sec/Mpc])."""
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

    def efunc(self, z: ArrayT | float, /) -> ArrayT:
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
