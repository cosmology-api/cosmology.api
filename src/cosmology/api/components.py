"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT
from cosmology.api.core import CosmologyAPI

__all__: list[str] = []


class GlobalCurvatureComponent(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains global curvature, described by :math:`Omega_K`."""

    @property
    def Ok0(self) -> ArrayT:
        """Omega curvature; the effective curvature density/critical density at z=0."""
        ...

    def Ok(self, z: ArrayT, /) -> ArrayT:
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


class MatterComponent(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains matter, described by :math:`Omega_m`."""

    @property
    def Om0(self) -> ArrayT:
        """Omega matter; matter density/critical density at z=0."""
        ...

    def Om(self, z: ArrayT, /) -> ArrayT:
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


class BaryonComponent(MatterComponent[ArrayT], Protocol):
    r"""The cosmology contains baryons, described by :math:`Omega_b`."""

    @property
    def Ob0(self) -> ArrayT:
        """Omega baryon; baryon density/critical density at z=0."""
        ...

    def Ob(self, z: ArrayT, /) -> ArrayT:
        """Redshift-dependent baryon density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...


class NeutrinoComponent(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains neutrinos, described by :math:`Omega_\nu`."""

    @property
    def Onu0(self) -> ArrayT:
        """Omega nu; the density/critical density of neutrinos at z=0."""
        ...

    @property
    def Neff(self) -> ArrayT:
        """Effective number of neutrino species."""
        ...

    @property
    def m_nu(self) -> tuple[ArrayT, ...]:
        """Neutrino mass in eV."""
        ...

    def Onu(self, z: ArrayT, /) -> ArrayT:
        r"""Redshift-dependent neutrino density parameter.

        Parameters
        ----------
        z : Array, positional-only
            Input redshift.

        Returns
        -------
        Array
        """
        ...


class DarkEnergyComponent(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains photons, described by :math:`Omega_{\rm de}`."""

    @property
    def Ode0(self) -> ArrayT:
        """Omega dark energy; dark energy density/critical density at z=0."""
        ...

    def Ode(self, z: ArrayT, /) -> ArrayT:
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


class DarkMatterComponent(MatterComponent[ArrayT], Protocol):
    r"""The cosmology contains cold dark matter, described by :math:`Omega_dm`."""

    @property
    def Odm0(self) -> ArrayT:
        """Omega dark matter; dark matter density/critical density at z=0."""
        ...

    def Odm(self, z: ArrayT, /) -> ArrayT:
        """Redshift-dependent dark matter density parameter.

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
        redshift of interest.
        """
        ...


class PhotonComponent(CosmologyAPI[ArrayT], Protocol):
    r"""The cosmology contains photons, described by :math:`Omega_\gamma`."""

    @property
    def Ogamma0(self) -> ArrayT:
        """Omega gamma; the density/critical density of photons at z=0."""
        ...

    def Ogamma(self, z: ArrayT, /) -> ArrayT:
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
