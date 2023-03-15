"""Test ``cosmology.api.HasHubbleParameter``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasHubbleParameter
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hubbleparametrized():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasHubbleParameter`.
    """
    # Simple example: missing everything

    class ExampleHasHubbleParameter:
        pass

    cosmo = ExampleHasHubbleParameter()

    assert not isinstance(cosmo, HasHubbleParameter)

    # TODO: more examples?


def test_compliant_hubbleparametrized(hashubbleparamet_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasHubbleParameter`.
    """
    ExampleHasHubbleParameter = make_dataclass(
        "ExampleHasHubbleParameter",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(hashubbleparamet_cls,),
        namespace={
            "h": _default_one,
            "hubble_time": _default_one,
            "hubble_distance": _default_one,
            "H": _return_1arg,
            "efunc": _return_1arg,
            "inv_efunc": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleHasHubbleParameter()

    assert isinstance(cosmo, HasHubbleParameter)


def test_fixture(hashubbleparamet_cls):
    """
    Test that the ``hashubbleparamet_cls`` fixture is a
    `cosmology.api.HasHubbleParameter`.
    """
    assert isinstance(hashubbleparamet_cls(), HasHubbleParameter)
