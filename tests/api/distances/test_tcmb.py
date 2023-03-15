"""Test ``cosmology.api._HasTcmb``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api._array_api import Array
from cosmology.api._distances import _HasTcmb

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hastcmbs():
    """
    Test that a non-compliant instance is not a
    `cosmology.api._HasTcmb`.
    """
    # Simple example: missing everything

    class Example_HasTcmb:
        pass

    cosmo = Example_HasTcmb()

    assert not isinstance(cosmo, _HasTcmb)

    # TODO: more examples?


def test_compliant_hastcmbs(hastcmb_cls):
    """
    Test that a compliant instance is a
    `cosmology.api._HasTcmb`.
    """
    Example_HasTcmb = make_dataclass(
        "Example_HasTcmb",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(hastcmb_cls,),
        namespace={
            "Tcmb0": _default_one,
            "Tcmb": _return_1arg,
        },
        frozen=True,
    )

    cosmo = Example_HasTcmb()

    assert isinstance(cosmo, _HasTcmb)


def test_fixture(hastcmb_cls):
    """
    Test that the ``hastcmb_cls`` fixture is a
    `cosmology.api._HasTcmb`.
    """
    assert isinstance(hastcmb_cls(), _HasTcmb)
