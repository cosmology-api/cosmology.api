"""Test ``cosmology_api.api.constants``."""

# STDLIB
from types import SimpleNamespace

# LOCAL
from cosmology.api import CosmologyConstantsAPINamespace

################################################################################
# TESTS
################################################################################


def test_noncompliant_namespace():
    """
    Test that a non-compliant namespace is not a
    `cosmology.api.CosmologyConstantsAPINamespace`.
    """
    example_namespace = SimpleNamespace()

    assert not isinstance(example_namespace, CosmologyConstantsAPINamespace)


def test_compliant_namespace():
    """
    Test that a compliant namespace is a
    `cosmology.api.CosmologyConstantsAPINamespace`.
    """
    example_namespace = SimpleNamespace(G=1)

    assert isinstance(example_namespace, CosmologyConstantsAPINamespace)


def test_fixture(constants_ns: CosmologyConstantsAPINamespace):
    """
    Test that the ``constants_ns`` fixture is a
    `cosmology.api.CosmologyConstantsAPINamespace`.
    """
    assert isinstance(constants_ns, CosmologyConstantsAPINamespace)
