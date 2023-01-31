"""Array API."""

from __future__ import annotations

from typing import TypeVar

from .array import Array  # noqa: TCH001

__all__: list[str] = []


ArrayT = TypeVar("ArrayT", bound=Array)
ArrayT_co = TypeVar("ArrayT_co", bound=Array, covariant=True)
