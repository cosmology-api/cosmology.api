"""Test ``cosmology_api.api.compat``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass

# THIRD-PARTY
import numpy.array_api as xp
import pytest

# LOCAL
from cosmology.api import (
    CosmologyAPIConformant,
    CosmologyAPIConformantWrapper,
    CosmologyAPINamespace,
)
from cosmology.api._array_api.array import ArrayAPIConformant as Array

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.FLRWAPIConformantWrapper`.
    """
    # Simple example: missing everything
    class FLRWWrapper:
        pass

    wrapper = FLRWWrapper()

    assert not isinstance(wrapper, CosmologyAPIConformantWrapper)

    # TODO: more examples?


def test_compliant_flrw(
    cosmology_ns: CosmologyAPINamespace,
    cosmology_cls: type[CosmologyAPIConformant],
):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyAPIConformantWrapper`. In particular, this tests
    that the class does not need to inherit from the Protocol to be compliant.
    """

    def return_one(self, /) -> Array:
        return xp.ones((), dtype=xp.int32)

    def return_1arg(self, z: Array, /) -> Array:
        return z

    @dataclass
    class CosmologyWrapper:

        cosmo: object

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

        def __getattr__(self, name: str) -> object:
            return getattr(self.cosmo, name)

        H0: Array = xp.ones((), dtype=xp.int32)
        Om0: Array = xp.ones((), dtype=xp.int32)
        Ode0: Array = xp.ones((), dtype=xp.int32)
        Tcmb0: Array = xp.ones((), dtype=xp.int32)
        Neff: Array = xp.ones((), dtype=xp.int32)
        m_nu: Array = xp.ones((), dtype=xp.int32)
        Ob0: Array = xp.ones((), dtype=xp.int32)

        scale_factor0 = property(return_one)
        h = property(return_one)
        hubble_distance = property(return_one)
        hubble_time = property(return_one)
        Otot0 = property(return_one)
        Odm0 = property(return_one)
        Ok0 = property(return_one)
        Ogamma0 = property(return_one)
        Onu0 = property(return_one)

        critical_density0 = property(return_one)
        rho_tot0 = property(return_one)
        rho_m0 = property(return_one)
        rho_de0 = property(return_one)
        rho_b0 = property(return_one)
        rho_dm0 = property(return_one)
        rho_k0 = property(return_one)
        rho_gamma0 = property(return_one)
        rho_nu0 = property(return_one)

        scale_factor = return_1arg
        H = return_1arg
        efunc = return_1arg
        inv_efunc = return_1arg
        Otot = return_1arg
        Om = return_1arg
        Ob = return_1arg
        Odm = return_1arg
        Ok = return_1arg
        Ode = return_1arg
        Ogamma = return_1arg
        Onu = return_1arg

        rho_critical = return_1arg
        rho_tot = return_1arg
        rho_m = return_1arg
        rho_de = return_1arg
        rho_k = return_1arg

        age = return_1arg
        lookback_time = return_1arg
        comoving_distance = return_1arg
        comoving_transverse_distance = return_1arg
        comoving_volume = return_1arg
        differential_comoving_volume = return_1arg

        angular_diameter_distance = return_1arg
        luminosity_distance = return_1arg

    wrapper = CosmologyWrapper(object())

    assert isinstance(wrapper, CosmologyAPIConformant)
    assert isinstance(wrapper, CosmologyAPIConformantWrapper)


class Test_CosmologyAPIConformantWrapper:
    @pytest.fixture(scope="class")
    def wrapper_cls(self, cosmology_ns):
        @dataclass(frozen=True)
        class CosmologyWrapper(CosmologyAPIConformantWrapper):

            cosmo: object

            def __cosmology_namespace__(
                self, /, *, api_version: str | None = None
            ) -> CosmologyAPINamespace:
                return cosmology_ns

            @property
            def name(self) -> str | None:
                return None

        return CosmologyWrapper

    @pytest.fixture(scope="class")
    def wrapper(self, cosmology, wrapper_cls):
        return wrapper_cls(cosmology)

    # =========================================================================
    # Tests

    def test_is_compliant(self, wrapper):
        """Test that the wrapper is compliant."""
        assert isinstance(wrapper, CosmologyAPIConformant)
        assert isinstance(wrapper, CosmologyAPIConformantWrapper)

    def test_getattr(self, wrapper):
        """Test that the wrapper can access the attributes of the wrapped object."""
        # Cosmology API
        assert wrapper.name is None

        # Not Cosmology API
        assert wrapper.not_cosmology_api == 1

        with pytest.raises(AttributeError):
            wrapper.this_is_not_an_attribute
