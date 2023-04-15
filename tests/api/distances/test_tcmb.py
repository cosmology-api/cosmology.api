"""Test ``cosmology.api.HasTcmb``."""

from __future__ import annotations

from dataclasses import field, make_dataclass

from cosmology.api._array_api import Array
from cosmology.api._distances import HasTcmb

from ..conftest import _default_one, _return_1arg

################################################################################
# TESTS
################################################################################


def test_noncompliant_hastcmbs():
    """
    Test that a non-compliant instance is not a
    `cosmology.api.HasTcmb`.
    """
    # Simple example: missing everything

    class ExampleHasTcmb:
        pass

    cosmo = ExampleHasTcmb()

    assert not isinstance(cosmo, HasTcmb)

    # TODO: more examples?


def test_compliant_hastcmbs(hastcmb_cls):
    """
    Test that a compliant instance is a
    `cosmology.api.HasTcmb`.
    """
    ExampleHasTcmb = make_dataclass(
        "ExampleHasTcmb",
        [(n, Array, field(default_factory=_default_one)) for n in {"H0"}],
        bases=(hastcmb_cls,),
        namespace={
            "T_cmb0": _default_one,
            "Tcmb": _return_1arg,
        },
        frozen=True,
    )

    cosmo = ExampleHasTcmb()

    assert isinstance(cosmo, HasTcmb)


def test_fixture(hastcmb_cls):
    """
    Test that the ``hastcmb_cls`` fixture is a
    `cosmology.api.HasTcmb`.
    """
    assert isinstance(hastcmb_cls(), HasTcmb)
