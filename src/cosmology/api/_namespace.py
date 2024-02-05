"""The Cosmology API Namespace.

This module describes the namespace of a Cosmology-API compatible library. There
should be the following required objects:

- constants: a module of constants. See :mod:`cosmology.api.constants` for
  details.

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

__all__: list[str] = []

if TYPE_CHECKING:
    from cosmology.api._constants import CosmologyConstantsNamespace


@runtime_checkable
class CosmologyNamespace(Protocol):
    """Runtime-checkable Protocol for the Cosmology API namespace.

    Examples
    --------
    A library can be checked for conformance with the Cosmology API namespace.

        >>> from cosmology.api import CosmologyNamespace
        >>> from astropy import cosmology as astropy_cosmology
        >>> isinstance(astropy_cosmology, CosmologyNamespace)
        False

    We can check what is missing from the library.

        >>> print(
        ...     set(n for n in dir(CosmologyNamespace) if not n.startswith('_'))
        ...     - set(dir(astropy_cosmology)))
        {'constants'}

    Most libraries are not yet Cosmology API compatible. There are compatibility
    wrappers to help with this, with documentation upcoming.

    Notes
    -----
    This is a Protocol, so it is not meant to be instantiated. It is meant to be
    used for static and runtime type checking. See
    https://docs.python.org/3/library/typing.html#typing.Protocol for more
    details.

    When used in a runtime check, `isinstance` will only look for the existence
    of objects, not details like their type. For example, ``constants`` should
    be a `~cosmology.api.CosmologyConstantsNamespace`, but `isinstance` will not
    check this.

    """

    @property
    def constants(self) -> CosmologyConstantsNamespace:
        """The cosmology constants API."""
        ...
