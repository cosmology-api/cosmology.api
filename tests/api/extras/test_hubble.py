"""Test ``cosmology.api.HubbleParameter``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HubbleParameter
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hubbleparametrized():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HubbleParameter`.
    """
    # Simple example: missing everything

    class ExampleHubbleParameter:
        pass

    cosmo = ExampleHubbleParameter()

    assert not isinstance(cosmo, HubbleParameter)

    # TODO: more examples?


def test_compliant_hubbleparametrized(hashubble_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HubbleParameter`.
    """
    ExampleHubbleParameter = make_dataclass(
        "ExampleHubbleParameter",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(hashubble_cls,),
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

    cosmo = ExampleHubbleParameter()

    assert isinstance(cosmo, HubbleParameter)


def test_fixture(hashubble_cls):
    """
    Test that the ``hashubble_cls`` fixture is a
    `cosmology.api.HubbleParameter`.
    """
    assert isinstance(hashubble_cls(), HubbleParameter)
