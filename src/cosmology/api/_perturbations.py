"""Cosmology API: perturbations, etc."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import Array
from cosmology.api._core import InputT


@runtime_checkable
class HasGrowthFactor(Protocol[Array, InputT]):
    r"""Cosmology has a growth factor :math:`D(z)`."""

    def growth_factor(self, z: InputT, /) -> Array:
        r"""Growth factor :math:`D(z)` at redshift :math:`z`.

        The growth factor :math:`D(z)` is defined such that, in linear
        theory, the power spectrum :math:`P(k, z)` at redshift :math:`z`
        is

        .. math::

           P(k, z) = [D(z)]^2 \, P(k, z=0) \;.

        In particular, this means that the growth factor is normalised
        today: :math:`D(0) \equiv 1`.

        .. caution::

           Other normalisations have been used in the past, for example,
           with respect to initial conditions.

        """
