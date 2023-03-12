"""Fixtures for the Cosmology API standard."""

from __future__ import annotations

from dataclasses import dataclass, make_dataclass

import pytest
from cosmology.api import (
    CosmologyAPINamespace,
    CosmologyWrapper,
    StandardCosmologyWrapper,
)

from ..conftest import (  # noqa: F401
    _return_1arg,
    _return_one,
    cosmology_ns,
    standard_attrs,
    standard_meths,
)

# ==============================================================================
# Cosmology API


@pytest.fixture(scope="session")
def cosmology_wrapper_cls(
    cosmology_ns: CosmologyAPINamespace,  # noqa: F811
) -> type[CosmologyWrapper]:
    """An example cosmology API wrapper class."""

    @dataclass(frozen=True)
    class CosmologyWrapper(CosmologyWrapper):
        """An example cosmology API wrapper class."""

        cosmo: object

        def __cosmology_namespace__(
            self, /, *, api_version: str | None = None
        ) -> CosmologyAPINamespace:
            return cosmology_ns

        @property
        def name(self) -> str | None:
            return None

    return CosmologyWrapper


# ==============================================================================
# Standard COSMOLOGY API


@pytest.fixture(scope="session")
def standardcosmo_wrapper_cls(
    cosmology_wrapper_cls: type[CosmologyWrapper],
    standard_attrs: set[str],  # noqa: F811
    standard_meths: set[str],  # noqa: F811
) -> type[StandardCosmologyWrapper]:
    """Example FLRW API wrapper class."""
    return make_dataclass(
        "FLRWWrapper",
        [("cosmo", object)],
        bases=(cosmology_wrapper_cls, StandardCosmologyWrapper),
        namespace={n: property(_return_one) for n in standard_attrs}
        | {n: _return_1arg for n in standard_meths},
        frozen=True,
    )
