"""The cosmology API."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import Array
from cosmology.api._core import InputT

__all__: list[str] = []


@runtime_checkable
class HasOmegaTot0(Protocol[Array]):
    r"""The object has a total density attribute -- :math:`Omega_{\rm tot}`."""

    @property
    def Omega_tot0(self) -> Array:
        r"""Omega total; the total density/critical density at z=0."""


@runtime_checkable
class HasOmegaTot(Protocol[Array, InputT]):
    r"""The object has a total density method."""

    def Omega_tot(self, z: InputT, /) -> Array:
        r"""Redshift-dependent total density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class TotalComponent(
    HasOmegaTot[Array, InputT],
    HasOmegaTot0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the total density."""


# ==============================================================================


@runtime_checkable
class HasOmegaK0(Protocol[Array]):
    r"""The object has a curvature density attribute -- :math:`Omega_K`."""

    @property
    def Omega_k0(self) -> Array:
        r"""Omega curvature; the effective curvature density/critical density at z=0."""


@runtime_checkable
class HasOmegaK(Protocol[Array, InputT]):
    r"""The object has a curvature density method."""

    def Omega_k(self, z: InputT, /) -> Array:
        r"""Redshift-dependent curvature density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class CurvatureComponent(
    HasOmegaK[Array, InputT],
    HasOmegaK0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the global curvature."""


# ==============================================================================


@runtime_checkable
class HasOmegaM0(Protocol[Array]):
    r"""The object has a matter density attribute -- :math:`Omega_m`."""

    @property
    def Omega_m0(self) -> Array:
        r"""Omega matter; the matter density/critical density at z=0."""


@runtime_checkable
class HasOmegaM(Protocol[Array, InputT]):
    r"""The object has a matter density method."""

    def Omega_m(self, z: InputT, /) -> Array:
        r"""Redshift-dependent matter density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest; see `Omega_nu`.

        """


@runtime_checkable
class MatterComponent(
    HasOmegaM[Array, InputT],
    HasOmegaM0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the matter density."""


# ==============================================================================


@runtime_checkable
class HasOmegaB0(Protocol[Array]):
    r"""The object has a baryon density attribute -- :math:`Omega_b`."""

    @property
    def Omega_b0(self) -> Array:
        r"""Omega baryon; the baryon density/critical density at z=0."""


@runtime_checkable
class HasOmegaB(Protocol[Array, InputT]):
    r"""The object has a baryon density method."""

    def Omega_b(self, z: InputT, /) -> Array:
        r"""Redshift-dependent baryon density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class BaryonComponent(
    HasOmegaB[Array, InputT],
    HasOmegaB0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the baryon density."""


# ==============================================================================


@runtime_checkable
class HasOmegaNu0(Protocol[Array]):
    r"""The object has a neutrino density attribute -- :math:`Omega_\nu`."""

    @property
    def Omega_nu0(self) -> Array:
        r"""Omega neutrino; the neutrino density/critical density at z=0."""


@runtime_checkable
class HasOmegaNu(Protocol[Array, InputT]):
    r"""The object has a neutrino density method."""

    def Omega_nu(self, z: InputT, /) -> Array:
        r"""Redshift-dependent neutrino density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class HasNeff(Protocol[Array]):
    r"""The object has an attribute for the effective number of neutrino species."""

    @property
    def Neff(self) -> Array:
        r"""Effective number of neutrino species."""


@runtime_checkable
class HasMNu(Protocol[Array]):
    r"""The object has a neutrino mass(es) attribute."""

    @property
    def m_nu(self) -> tuple[Array, ...]:
        r"""Neutrino mass(es) in eV."""


@runtime_checkable
class NeutrinoComponent(
    HasOmegaNu[Array, InputT],
    HasMNu[Array],
    HasNeff[Array],
    HasOmegaNu0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the neutrino density."""


# ==============================================================================


@runtime_checkable
class HasOmegaDE0(Protocol[Array]):
    r"""The object has a dark energy density attribute -- :math:`Omega_{\rm de}`."""

    @property
    def Omega_de0(self) -> Array:
        r"""Omega dark energy; the dark energy density/critical density at z=0."""


@runtime_checkable
class HasOmegaDE(Protocol[Array, InputT]):
    r"""The object has a dark energy density method."""

    def Omega_de(self, z: InputT, /) -> Array:
        r"""Redshift-dependent dark energy density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class DarkEnergyComponent(HasOmegaDE[Array, InputT], HasOmegaDE0[Array], Protocol):
    r"""The cosmology has attributes and methods for the dark energy."""


# ==============================================================================


@runtime_checkable
class HasOmegaDM0(Protocol[Array]):
    r"""The object has a dark matter density attribute -- :math:`Omega_{\rm dm}`."""

    @property
    def Omega_dm0(self) -> Array:
        r"""Omega dark matter; the dark matter density/critical density at z=0."""


@runtime_checkable
class HasOmegaDM(Protocol[Array, InputT]):
    r"""The object has a dark matter density method."""

    def Omega_dm(self, z: InputT, /) -> Array:
        r"""Redshift-dependent dark matter density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        Notes
        -----
        This does not include neutrinos, even if non-relativistic at the
        redshift of interest.

        """


@runtime_checkable
class DarkMatterComponent(
    HasOmegaDM[Array, InputT],
    HasOmegaDM0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the dark matter."""


# ==============================================================================


@runtime_checkable
class HasOmegaGamma0(Protocol[Array]):
    r"""The object has a photon density attribute -- :math:`Omega_\gamma`."""

    @property
    def Omega_gamma0(self) -> Array:
        r"""Omega gamma; the photon density/critical density at z=0."""


@runtime_checkable
class HasOmegaGamma(Protocol[Array, InputT]):
    r"""The object has a photon density method."""

    def Omega_gamma(self, z: InputT, /) -> Array:
        r"""Redshift-dependent photon density parameter.

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array

        """


@runtime_checkable
class PhotonComponent(
    HasOmegaGamma[Array, InputT],
    HasOmegaGamma0[Array],
    Protocol,
):
    r"""The cosmology has attributes and methods for the photons."""
