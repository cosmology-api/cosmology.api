from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    # STDLIB
    from types import EllipsisType
    from typing import Self

    # LOCAL
    from .dtype import DTypeConformant


__all__: list[str] = []


@runtime_checkable
class Array(Protocol):
    """Runtime checkable protocol for conformance with the array API."""

    @property
    def dtype(self) -> DTypeConformant:
        """Data type of the array elements."""
        ...

    @property
    def ndim(self) -> int:
        """Number of array dimensions (axes)."""
        ...

    @property
    def shape(self) -> tuple[int | None, ...]:
        """Array dimensions."""
        ...

    @property
    def size(self) -> int | None:
        """Number of elements in an array."""
        ...

    @property
    def T(self: Self) -> Self:
        """Transpose of the array."""
        ...

    def __abs__(self: Self, /) -> Self:
        """Calculates the absolute value for each element of an array instance."""
        ...

    def __add__(self: Self, other: float | Self, /) -> Self:
        """
        Calculates the sum for each element of an array instance with the
        respective element of the array ``other``.
        """
        ...

    def __bool__(self, /) -> bool:
        """Converts a zero-dimensional boolean array to a Python ``bool`` object."""
        ...

    def __eq__(self: Self, other: object, /) -> Self:  # type: ignore[override]
        """
        Computes the truth value of ``self_i == other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __float__(self) -> float:
        """
        Converts a zero-dimensional floating-point array to a Python ``float``
        object.
        """
        ...

    def __floordiv__(self: Self, other: float | Self, /) -> Self:
        """
        Evaluates ``self_i // other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...

    def __ge__(self: Self, other: float | Self, /) -> Self:
        """
        Computes the truth value of ``self_i >= other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __getitem__(
        self: Self,
        key: int | slice | EllipsisType | tuple[int | slice | EllipsisType, ...] | Self,
        /,
    ) -> Self:
        """Returns ``self[key]``."""
        ...

    def __gt__(self: Self, other: float | Self, /) -> Self:
        """
        Computes the truth value of ``self_i > other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __index__(self, /) -> int:
        """Converts a zero-dimensional integer array to a Python ``int`` object."""
        ...

    def __int__(self, /) -> int:
        """Converts a zero-dimensional integer array to a Python ``int`` object."""
        ...

    def __invert__(self: Self, /) -> Self:
        """Evaluates ``~self_i`` for each element of an array instance."""
        ...

    def __le__(self: Self, other: float | Self, /) -> Self:
        """
        Computes the truth value of ``self_i <= other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __lshift__(self: Self, other: int | Self, /) -> Self:
        """
        Evaluates ``self_i << other_i`` for each element of an array instance
        with the respective element  of the array ``other``.
        """
        ...

    def __lt__(self: Self, other: float | Self, /) -> Self:
        """
        Computes the truth value of ``self_i < other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __matmul__(self: Self, other: Self, /) -> Self:
        """Computes the matrix product."""
        ...

    def __mod__(self: Self, other: float | Self, /) -> Self:
        """
        Evaluates ``self_i % other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...

    def __mul__(self: Self, other: float | Self, /) -> Self:
        """
        Calculates the product for each element of an array instance with the
        respective element of the array ``other``.
        """
        ...

    def __ne__(self: Self, other: object, /) -> Self:  # type: ignore[override]
        """
        Computes the truth value of ``self_i != other_i`` for each element of an
        array instance with the respective element of the array ``other``.
        """
        ...

    def __neg__(self: Self, /) -> Self:
        """Evaluates ``-self_i`` for each element of an array instance."""
        ...

    def __or__(self: Self, other: object, /) -> Self:
        """
        Evaluates ``self_i | other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...

    def __pos__(self: Self, /) -> Self:
        """Evaluates ``+self_i`` for each element of an array instance."""
        ...

    def __pow__(self: Self, other: float | Self, /) -> Self:
        """
        Calculates an implementation-dependent approximation of exponentiation
        by raising each element (the base) of an array instance to the power of
        ``other_i`` (the exponent), where ``other_i`` is the corresponding
        element of the array ``other``.
        """
        ...

    def __rshift__(self: Self, other: int | Self, /) -> Self:
        """
        Evaluates ``self_i >> other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...

    def __setitem__(
        self: Self,
        key: (
            int | slice | EllipsisType | tuple[int | slice | EllipsisType, ...] | Array
        ),
        value: float | bool | Self,
        /,
    ) -> None:
        """Sets ``self[key]`` to ``value``."""
        ...

    def __sub__(self: Self, other: float | Self, /) -> Self:
        """
        Calculates the difference for each element of an array instance with the
        respective element of the array ``other``. The result of ``self_i -
        other_i`` must be the same as ``self_i + (-other_i)`` and must be
        governed by the same floating-point rules as addition (see
        :meth:`array.__add__`).
        """
        ...

    def __truediv__(self: Self, other: float | Self, /) -> Self:
        """
        Evaluates ``self_i / other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...

    def __xor__(self: Self, other: int | bool | Self, /) -> Self:
        """
        Evaluates ``self_i ^ other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        """
        ...
