"""The cosmology constants API.

The list of required constants is:

- G: Gravitational constant G in pc km2 s-2 Msol-1.
- c: Speed of light in km s-1.

"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

__all__: list[str] = []


@runtime_checkable
class CosmologyConstantsNamespace(Protocol):
    """Runtime-checkable Protocol for the Cosmology API constants module.

    Examples
    --------
    A module can be checked for conformance with the Cosmology API's constants
    namespace.

        >>> from types import SimpleNamespace
        >>> constants = SimpleNamespace(G=1, c=2)
        >>> isinstance(constants, CosmologyConstantsNamespace)
        True

        >>> constants.G
        1

    Most cosmology libraries are not yet Cosmology API compatible. There are
    compatibility wrappers to help with this, with documentation upcoming.

    Notes
    -----
    This is a Protocol, so it is not meant to be instantiated. It is meant to be
    used for static and runtime type checking. See
    https://docs.python.org/3/library/typing.html#typing.Protocol for more
    details.

    When used in a runtime check, `isinstance` will only look for the existence
    of objects, not details like their type. For example, ``c`` should be in
    units of kilometers per second, but `isinstance` will not check this.

    """

    @property
    def G(self) -> Any:  # noqa: ANN401
        """Gravitational constant G in pc km2 s-2 Msol-1."""
        ...

    @property
    def c(self) -> Any:  # noqa: ANN401
        """Speed of light in km s-1."""
        ...
