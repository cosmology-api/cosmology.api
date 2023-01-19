"""Test ``cosmology_api.api.compat``."""

from __future__ import annotations

# STDLIB
from dataclasses import dataclass

# LOCAL
from cosmology.api import (
    CosmologyAPIConformant,
    CosmologyAPIConformantWrapper,
    CosmologyAPINamespace,
)

################################################################################
# TESTS
################################################################################


def test_noncompliant_cosmology_wrapper():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.CosmologyAPIConformantWrapper`.
    """
    # Simple example: missing everything
    class CosmologyWrapper:
        pass

    wrapper = CosmologyWrapper()

    assert not isinstance(wrapper, CosmologyAPIConformantWrapper)

    # TODO: more examples?


def test_compliant_cosmology(
    cosmology_ns: CosmologyAPINamespace, cosmology: CosmologyAPIConformant
):
    """
    Test that a compliant instance is a
    `cosmology.api.CosmologyAPIConformantWrapper`.
    """

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

    wrapper = CosmologyWrapper(cosmology)

    assert isinstance(wrapper, CosmologyAPIConformant)
    assert isinstance(wrapper, CosmologyAPIConformantWrapper)
