"""The cosmology API."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT_co
from cosmology.api._core import Cosmology, InputT_contra

__all__: list[str] = []


@runtime_checkable
class HasOmegaTot0(Protocol[ArrayT_co]):
    r"""The object has a total density attribute -- :math:`Omega_{\rm tot}`."""

    @property
    def Omega_tot0(self) -> ArrayT_co:
        r"""Omega total; the total density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaTot(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a total density method."""

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


@runtime_checkable
class HasTotalComponent(
    HasOmegaTot[ArrayT_co, InputT_contra],
    HasOmegaTot0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the total density."""


# ==============================================================================


@runtime_checkable
class HasOmegaK0(Protocol[ArrayT_co]):
    r"""The object has a curvature density attribute -- :math:`Omega_K`."""

    @property
    def Omega_k0(self) -> ArrayT_co:
        r"""Omega curvature; the effective curvature density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaK(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a curvature density method."""

    def Omega_k(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent curvature density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class HasGlobalCurvatureComponent(
    HasOmegaK[ArrayT_co, InputT_contra],
    HasOmegaK0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the global curvature."""


# ==============================================================================


@runtime_checkable
class HasOmegaM0(Protocol[ArrayT_co]):
    r"""The object has a matter density attribute -- :math:`Omega_m`."""

    @property
    def Omega_m0(self) -> ArrayT_co:
        r"""Omega matter; the matter density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaM(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a matter density method."""

    def Omega_m(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent matter density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest; see `Omega_nu`.
        """
        ...


@runtime_checkable
class HasMatterComponent(
    HasOmegaM[ArrayT_co, InputT_contra],
    HasOmegaM0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the matter density."""


# ==============================================================================


@runtime_checkable
class HasOmegaB0(Protocol[ArrayT_co]):
    r"""The object has a baryon density attribute -- :math:`Omega_b`."""

    @property
    def Omega_b0(self) -> ArrayT_co:
        r"""Omega baryon; the baryon density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaB(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a baryon density method."""

    def Omega_b(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent baryon density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class HasBaryonComponent(
    HasOmegaB[ArrayT_co, InputT_contra],
    HasOmegaB0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the baryon density."""


# ==============================================================================


@runtime_checkable
class HasOmegaNu0(Protocol[ArrayT_co]):
    r"""The object has a neutrino density attribute -- :math:`Omega_\nu`."""

    @property
    def Omega_nu0(self) -> ArrayT_co:
        r"""Omega neutrino; the neutrino density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaNu(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a neutrino density method."""

    def Omega_nu(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent neutrino density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class HasNeff(Protocol[ArrayT_co]):
    r"""The object has an attribute for the effective number of neutrino species."""

    @property
    def Neff(self) -> ArrayT_co:
        r"""Effective number of neutrino species."""
        ...


@runtime_checkable
class HasMNu(Protocol[ArrayT_co]):
    r"""The object has a neutrino mass(es) attribute."""

    @property
    def m_nu(self) -> tuple[ArrayT_co, ...]:
        r"""Neutrino mass(es) in eV."""
        ...


@runtime_checkable
class HasNeutrinoComponent(
    HasOmegaNu[ArrayT_co, InputT_contra],
    HasMNu[ArrayT_co],
    HasNeff[ArrayT_co],
    HasOmegaNu0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the neutrino density."""


# ==============================================================================


@runtime_checkable
class HasOmegaDE0(Protocol[ArrayT_co]):
    r"""The object has a dark energy density attribute -- :math:`Omega_{\rm de}`."""

    @property
    def Omega_de0(self) -> ArrayT_co:
        r"""Omega dark energy; the dark energy density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaDE(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a dark energy density method."""

    def Omega_de(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent dark energy density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class HasDarkEnergyComponent(
    HasOmegaDE[ArrayT_co, InputT_contra],
    HasOmegaDE0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the dark energy."""


# ==============================================================================


@runtime_checkable
class HasOmegaDM0(Protocol[ArrayT_co]):
    r"""The object has a dark matter density attribute -- :math:`Omega_{\rm dm}`."""

    @property
    def Omega_dm0(self) -> ArrayT_co:
        r"""Omega dark matter; the dark matter density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaDM(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a dark matter density method."""

    def Omega_dm(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent dark matter density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest.
        """
        ...


@runtime_checkable
class HasDarkMatterComponent(
    HasOmegaDM[ArrayT_co, InputT_contra],
    HasOmegaDM0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the dark matter."""


# ==============================================================================


@runtime_checkable
class HasOmegaGamma0(Protocol[ArrayT_co]):
    r"""The object has a photon density attribute -- :math:`Omega_\gamma`."""

    @property
    def Omega_gamma0(self) -> ArrayT_co:
        r"""Omega gamma; the photon density/critical density at z=0."""
        ...


@runtime_checkable
class HasOmegaGamma(Protocol[ArrayT_co, InputT_contra]):
    r"""The object has a photon density method."""

    def Omega_gamma(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent photon density parameter.

        Parameters
        ----------
        z : Array
            Input redshifts.

        Returns
        -------
        Array
        """
        ...


@runtime_checkable
class HasPhotonComponent(
    HasOmegaGamma[ArrayT_co, InputT_contra],
    HasOmegaGamma0[ArrayT_co],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    r"""The cosmology has attributes and methods for the photons."""
