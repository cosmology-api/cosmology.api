from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, TypeVar, runtime_checkable

if TYPE_CHECKING:
    from typing import Self

    DType = TypeVar("DType", bound="DTypeConformant")

__all__: list[str] = []


@runtime_checkable
class DTypeConformant(Protocol):
    """Runtime-checkable protocol for the dtype."""

    def __eq__(self, other: Self, /) -> bool:
        """
        Computes the truth value of ``self == other`` in order to test for data
        type object equality.

        Parameters
        ----------
        self: dtype
            data type instance. May be any supported data type.
        other: dtype
            other data type instance. May be any supported data type.

        Returns
        -------
        out: bool
            a boolean indicating whether the data type objects are equal.

        """
        ...
