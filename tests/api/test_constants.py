"""Test ``cosmology.api.constants``."""
from __future__ import annotations

from types import SimpleNamespace

from cosmology.api import CosmologyConstantsNamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_namespace():
    """
    Test that a non-compliant namespace is not a
    `cosmology.api.CosmologyConstantsNamespace`.
    """
    example_namespace = SimpleNamespace()

    assert not isinstance(example_namespace, CosmologyConstantsNamespace)


def test_compliant_namespace():
    """
    Test that a compliant namespace is a
    `cosmology.api.CosmologyConstantsNamespace`.
    """
    example_namespace = SimpleNamespace(G=1, c=2)

    assert isinstance(example_namespace, CosmologyConstantsNamespace)


def test_fixture(constants_ns):
    """
    Test that the ``constants_ns`` fixture is a
    `cosmology.api.CosmologyConstantsNamespace`.
    """
    assert isinstance(constants_ns, CosmologyConstantsNamespace)
