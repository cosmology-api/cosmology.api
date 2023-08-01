"""Array API."""

from __future__ import annotations

from typing import TypeVar

from .array import Array as _Array

__all__: list[str] = []


Array = TypeVar("Array", bound=_Array, covariant=True)  # noqa: PLC0105
