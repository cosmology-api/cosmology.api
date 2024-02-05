"""Test ``cosmology.api.namespace``."""

from __future__ import annotations

from types import SimpleNamespace

from cosmology.api import CosmologyNamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_namespace():
    """
    Test that a non-compliant namespace is not a
    `cosmology.api.CosmologyNamespace`.
    """
    example_namespace = SimpleNamespace()

    assert not isinstance(example_namespace, CosmologyNamespace)


def test_compliant_namespace():
    """
    Test that a compliant namespace is a
    `cosmology.api.CosmologyNamespace`.
    """
    constants_namespace = SimpleNamespace(G=1)
    example_namespace = SimpleNamespace(constants=constants_namespace)

    assert isinstance(example_namespace, CosmologyNamespace)


def test_fixture(cosmology_ns):
    """
    Test that the ``cosmology_ns`` fixture is a
    `cosmology.api.CosmologyNamespace`.
    """
    assert isinstance(cosmology_ns, CosmologyNamespace)
