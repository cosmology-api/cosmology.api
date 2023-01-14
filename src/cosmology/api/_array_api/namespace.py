"""
Types for annotations.

The type variables should be replaced with the actual types for a given
library, e.g., for NumPy TypeVar('array') would be replaced with ndarray.
"""
from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

if TYPE_CHECKING:
    # STDLIB
    from collections.abc import Sequence

    # LOCAL
    from .array import ArrayAPIConformant
    from .device import DeviceConformant
    from .dtype import DTypeConformant
    from .linalg import ArrayAPILinAlgNamespace

SupportsBufferProtocol = Any
PyCapsule = Any
_T_co = TypeVar("_T_co", covariant=True)


class finfo_object(Protocol):
    """object returned by finfo."""

    bits: int
    eps: float
    max: float
    min: float
    smallest_normal: float


class iinfo_object(Protocol):
    """object returned by iinfo."""

    bits: int
    max: int
    min: int


class NestedSequence(Protocol[_T_co]):
    """Nested sequence."""

    def __getitem__(self, key: int, /) -> _T_co | NestedSequence[_T_co]:
        ...

    def __len__(self, /) -> int:
        ...


class ArrayAPINamespace(Protocol):
    """Runtime checkable protocol for the Array API namespace."""

    # ===============================================================
    # Constants

    @property
    def e(self) -> float:
        ...

    @property
    def inf(self) -> float:
        ...

    @property
    def nan(self) -> float:
        ...

    @property
    def newaxis(self) -> float:
        ...

    @property
    def pi(self) -> float:
        ...

    # ===============================================================
    # Creation Functions

    @staticmethod
    def arange(
        start: int | float,
        /,
        stop: int | float | None = None,
        step: int | float = 1,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def asarray(
        obj: ArrayAPIConformant
        | bool
        | int
        | float
        | NestedSequence[bool | int | float]
        | SupportsBufferProtocol,
        /,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
        copy: bool | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def empty_like(
        x: ArrayAPIConformant,
        /,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def eye(
        n_rows: int,
        n_cols: int | None = None,
        /,
        *,
        k: int = 0,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def from_dlpack(x: object, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def full(
        shape: int | tuple[int, ...],
        fill_value: int | float,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def full_like(
        x: ArrayAPIConformant,
        /,
        fill_value: int | float,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def linspace(
        start: int | float,
        stop: int | float,
        /,
        num: int,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
        endpoint: bool = True,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def meshgrid(
        *arrays: ArrayAPIConformant, indexing: str = "xy"
    ) -> list[ArrayAPIConformant]:
        ...

    @staticmethod
    def ones(
        shape: int | tuple[int, ...],
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def ones_like(
        x: ArrayAPIConformant,
        /,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def tril(x: ArrayAPIConformant, /, *, k: int = 0) -> ArrayAPIConformant:
        ...

    @staticmethod
    def triu(x: ArrayAPIConformant, /, *, k: int = 0) -> ArrayAPIConformant:
        ...

    @staticmethod
    def zeros(
        shape: int | tuple[int, ...],
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def zeros_like(
        x: ArrayAPIConformant,
        /,
        *,
        dtype: DTypeConformant | None = None,
        device: DeviceConformant | None = None,
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Data Type Functions

    @staticmethod
    def astype(
        x: ArrayAPIConformant, dtype: DTypeConformant, /, *, copy: bool = True
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def broadcast_arrays(*arrays: ArrayAPIConformant) -> list[ArrayAPIConformant]:
        ...

    @staticmethod
    def broadcast_to(
        x: ArrayAPIConformant, /, shape: tuple[int, ...]
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def can_cast(
        from_: DTypeConformant | ArrayAPIConformant, to: DTypeConformant, /
    ) -> bool:
        ...

    @staticmethod
    def finfo(type: DTypeConformant | ArrayAPIConformant, /) -> finfo_object:
        ...

    @staticmethod
    def iinfo(type: DTypeConformant | ArrayAPIConformant, /) -> iinfo_object:
        ...

    @staticmethod
    def result_type(
        *arrays_and_dtypes: ArrayAPIConformant | DTypeConformant,
    ) -> DTypeConformant:
        ...

    # ===============================================================
    # Elementwise Functions

    @staticmethod
    def abs(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def acos(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def acosh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def add(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def asin(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def asinh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def atan(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def atan2(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def atanh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_and(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_left_shift(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_invert(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_or(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_right_shift(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def bitwise_xor(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def ceil(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def cos(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def cosh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def divide(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def equal(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def exp(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def expm1(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def floor(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def floor_divide(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def greater(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def greater_equal(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def isfinite(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def isinf(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def isnan(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def less(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def less_equal(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def log(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def log1p(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def log2(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def log10(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def logaddexp(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def logical_and(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def logical_not(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def logical_or(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def logical_xor(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def multiply(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def negative(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def not_equal(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def positive(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def pow(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def remainder(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def round(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sign(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sin(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sinh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def square(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sqrt(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def subtract(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def tan(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def tanh(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def trunc(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Linalg

    @property
    def linalg(self) -> ArrayAPILinAlgNamespace:
        ...

    @staticmethod
    def matmul(x1: ArrayAPIConformant, x2: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    @staticmethod
    def matrix_transpose(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
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
    def vecdot(
        x1: ArrayAPIConformant, x2: ArrayAPIConformant, /, *, axis: int = -1
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Manipulation

    @staticmethod
    def concat(
        arrays: tuple[ArrayAPIConformant, ...] | list[ArrayAPIConformant],
        /,
        *,
        axis: int | None = 0,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def expand_dims(x: ArrayAPIConformant, /, *, axis: int = 0) -> ArrayAPIConformant:
        ...

    @staticmethod
    def flip(
        x: ArrayAPIConformant, /, *, axis: int | tuple[int, ...] | None = None
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def permute_dims(
        x: ArrayAPIConformant, /, axes: tuple[int, ...]
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def reshape(
        x: ArrayAPIConformant, /, shape: tuple[int, ...], *, copy: bool | None = None
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def roll(
        x: ArrayAPIConformant,
        /,
        shift: int | tuple[int, ...],
        *,
        axis: int | tuple[int, ...] | None = None,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def squeeze(
        x: ArrayAPIConformant, /, axis: int | tuple[int, ...]
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def stack(
        arrays: tuple[ArrayAPIConformant, ...] | list[ArrayAPIConformant],
        /,
        *,
        axis: int = 0,
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Searching

    @staticmethod
    def argmax(
        x: ArrayAPIConformant, /, *, axis: int | None = None, keepdims: bool = False
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def argmin(
        x: ArrayAPIConformant, /, *, axis: int | None = None, keepdims: bool = False
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def nonzero(x: ArrayAPIConformant, /) -> tuple[ArrayAPIConformant, ...]:
        ...

    @staticmethod
    def where(
        condition: ArrayAPIConformant, x1: ArrayAPIConformant, x2: ArrayAPIConformant, /
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Set

    @staticmethod
    def unique_all(
        x: ArrayAPIConformant, /
    ) -> tuple[
        ArrayAPIConformant, ArrayAPIConformant, ArrayAPIConformant, ArrayAPIConformant
    ]:
        ...

    @staticmethod
    def unique_counts(
        x: ArrayAPIConformant, /
    ) -> tuple[ArrayAPIConformant, ArrayAPIConformant]:
        ...

    @staticmethod
    def unique_inverse(
        x: ArrayAPIConformant, /
    ) -> tuple[ArrayAPIConformant, ArrayAPIConformant]:
        ...

    @staticmethod
    def unique_values(x: ArrayAPIConformant, /) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Sort

    @staticmethod
    def argsort(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sort(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Statistical

    @staticmethod
    def max(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def mean(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def min(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def prod(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        dtype: DTypeConformant | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def std(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        correction: int | float = 0.0,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def sum(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        dtype: DTypeConformant | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def var(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        correction: int | float = 0.0,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    # ===============================================================
    # Utility

    @staticmethod
    def all(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...

    @staticmethod
    def any(
        x: ArrayAPIConformant,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPIConformant:
        ...
