"""Test ``cosmology.api.HasHubbleMethods``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api import HasHubbleMethods
from cosmology.api._array_api import Array

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hubbleparametrized():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasHubbleMethods`.
    """
    # Simple example: missing everything

    class ExampleHasHubbleMethods:
        pass

    cosmo = ExampleHasHubbleMethods()

    assert not isinstance(cosmo, HasHubbleMethods)

    # TODO: more examples?


def test_compliant_hubbleparametrized(hashubble_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasHubbleMethods`.
    """
    ExampleHasHubbleMethods = make_dataclass(
        "ExampleHasHubbleMethods",
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

    cosmo = ExampleHasHubbleMethods()

    assert isinstance(cosmo, HasHubbleMethods)


def test_fixture(hashubble_cls):
    """
    Test that the ``hashubble_cls`` fixture is a
    `cosmology.api.HasHubbleMethods`.
    """
    assert isinstance(hashubble_cls(), HasHubbleMethods)
