from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Literal, Protocol

if TYPE_CHECKING:
    # STDLIB
    from collections.abc import Sequence

    # THIRD-PARTY
    from array_api.array import ArrayAPIConformant

__all__: list[str] = []


class ArrayAPILinAlgNamespace(Protocol):
    """Runtime-checkable protocol for linear algebra namespace."""

    @staticmethod
    def cholesky(
        x: ArrayAPIConformant, /, *, upper: bool = False
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def cross(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /, *, axis: int = -1
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def det(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def diagonal(x: ArrayAPIConformant, /, *, offset: int = 0) -> ArrayAPIConformant:
        ...

    @staticmethod
    def eigh(x: ArrayAPIConformant, /) -> tuple[ArrayAPIConformant]:
        ...

    @staticmethod
    def eigvalsh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def inv(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matmul(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matrix_norm(
        x: ArrayAPIConformant,
        /,
        *,
        keepdims: bool = False,
        ord: int | float | Literal["fro", "nuc"] | None = "fro",
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matrix_power(x: ArrayAPIConformant, n: int, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matrix_rank(
        x: ArrayAPIConformant, /, *, rtol: float | ArrayAPIConformant | None = None
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matrix_transpose(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def outer(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def pinv(
        x: ArrayAPIConformant, /, *, rtol: float | ArrayAPIConformant | None = None
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def qr(
        x: ArrayAPIConformant, /, *, mode: Literal["reduced", "complete"] = "reduced"
    ) -> tuple[ArrayAPIConformant, ArrayAPIConformant]:
        ...

    @staticmethod
    def slogdet(
        x: ArrayAPIConformant, /
    ) -> tuple[ArrayAPIConformant, ArrayAPIConformant]:
        ...

    @staticmethod
    def solve(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def svd(
        x: ArrayAPIConformant, /, *, full_matrices: bool = True
    ) -> ArrayAPIConformant | tuple[ArrayAPIConformant, ...]:
        ...

    @staticmethod
    def svdvals(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def tensordot(
        x1: ArrayAPIConformant,
        x2: ArrayAPIConformant,
        /,
        *,
        axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def trace(x: ArrayAPIConformant, /, *, offset: int = 0) -> ArrayAPIConformant:
        ...

    @staticmethod
    def vecdot(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /, *, axis: int = -1
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def vector_norm(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
        ord: int | float = 2,
    ) -> ArrayAPIConformant:
        ...
