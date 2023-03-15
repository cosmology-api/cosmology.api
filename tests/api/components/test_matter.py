"""Test ``cosmology.api.HasMatterComponent``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasMatterComponent
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_mattercomponent():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasMatterComponent`.
    """
    # Simple example: missing everything

    class ExampleHasMatterComponent:
        pass

    cosmo = ExampleHasMatterComponent()

    assert not isinstance(cosmo, HasMatterComponent)

    # TODO: more examples?


def test_compliant_mattercomponent(dists_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasMatterComponent`.
    """
    ExampleHasMatterComponent = make_dataclass(
        "ExampleHasMatterComponent",
        [(n, Array, field(default_factory=_default_one)) for n in {"Omega_m0"}],
        bases=(dists_cls,),
        namespace={"Omega_m": _return_1arg},
        frozen=True,
    )

    cosmo = ExampleHasMatterComponent()

    assert isinstance(cosmo, HasMatterComponent)


def test_fixture(matter_cls):
    """
    Test that the ``matter_cls`` fixture is a
    `cosmology.api.HasMatterComponent`.
    """
    assert isinstance(matter_cls(), HasMatterComponent)
