"""The cosmology API."""

from __future__ import annotations

from typing import Protocol

from cosmology.api._array_api import ArrayT_co
from cosmology.api._core import Cosmology, InputT_contra

__all__: list[str] = []


class HasTotalComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains a total density, described by :math:`Omega_{\rm tot}`."""

    @property
    def Omega_tot0(self) -> ArrayT_co:
        r"""Omega total; the total density/critical density at z=0."""
        ...

    def Omega_tot(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasGlobalCurvatureComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains global curvature, described by :math:`Omega_k`."""

    @property
    def Omega_k0(self) -> ArrayT_co:
        """Omega curvature; the effective curvature density/critical density at z=0."""
        ...

    def Omega_k(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasMatterComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains matter, described by :math:`Omega_m`."""

    @property
    def Omega_m0(self) -> ArrayT_co:
        """Omega matter; matter density/critical density at z=0."""
        ...

    def Omega_m(self, z: InputT_contra, /) -> ArrayT_co:
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
        redshift of interest; see `Omega_nu`.
        """
        ...


class HasBaryonComponent(HasMatterComponent[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains baryons, described by :math:`Omega_b`."""

    @property
    def Omega_b0(self) -> ArrayT_co:
        """Omega baryon; baryon density/critical density at z=0."""
        ...

    def Omega_b(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasNeutrinoComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains neutrinos, described by :math:`Omega_\nu`."""

    @property
    def Omega_nu0(self) -> ArrayT_co:
        """Omega nu; the density/critical density of neutrinos at z=0."""
        ...

    @property
    def Neff(self) -> ArrayT_co:
        """Effective number of neutrino species."""
        ...

    @property
    def m_nu(self) -> tuple[ArrayT_co, ...]:
        """Neutrino mass in eV."""
        ...

    def Omega_nu(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasDarkEnergyComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains photons, described by :math:`Omega_{\rm de}`."""

    @property
    def Omega_de0(self) -> ArrayT_co:
        """Omega dark energy; dark energy density/critical density at z=0."""
        ...

    def Omega_de(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasDarkMatterComponent(HasMatterComponent[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains cold dark matter, described by :math:`Omega_{\rm dm}`."""

    @property
    def Omega_dm0(self) -> ArrayT_co:
        """Omega dark matter; dark matter density/critical density at z=0."""
        ...

    def Omega_dm(self, z: InputT_contra, /) -> ArrayT_co:
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


class HasPhotonComponent(Cosmology[ArrayT_co, InputT_contra], Protocol):
    r"""The cosmology contains photons, described by :math:`Omega_\gamma`."""

    @property
    def Omega_gamma0(self) -> ArrayT_co:
        """Omega gamma; the density/critical density of photons at z=0."""
        ...

    def Omega_gamma(self, z: InputT_contra, /) -> ArrayT_co:
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
