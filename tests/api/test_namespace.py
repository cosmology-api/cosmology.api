"""Test ``cosmology_api.api.namespace``."""

# STDLIB
from types import SimpleNamespace

# LOCAL
from cosmology.api import CosmologyAPINamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_namespace():
    """
    Test that a non-compliant namespace is not a
    `cosmology.api.CosmologyAPINamespace`.
    """
    example_namespace = SimpleNamespace()

    assert not isinstance(example_namespace, CosmologyAPINamespace)


def test_compliant_namespace():
    """
    Test that a compliant namespace is a
    `cosmology.api.CosmologyAPINamespace`.
    """
    constants_namespace = SimpleNamespace(G=1)
    example_namespace = SimpleNamespace(constants=constants_namespace)

    assert isinstance(example_namespace, CosmologyAPINamespace)


def test_fixture(cosmology_ns):
    """
    Test that the ``cosmology_ns`` fixture is a
    `cosmology.api.CosmologyAPINamespace`.
    """
    assert isinstance(cosmology_ns, CosmologyAPINamespace)
