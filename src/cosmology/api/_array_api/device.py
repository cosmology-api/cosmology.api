from __future__ import annotations

# STDLIB
from typing import Protocol, TypeVar, runtime_checkable

__all__: list[str] = []

Device = TypeVar("Device", bound="DeviceConformant")


@runtime_checkable
class DeviceConformant(Protocol):
    """Runtime-checkable protocol for the dtype."""

    def __eq__(self: Device, other: Device, /) -> bool:
        """
        Computes the truth value of ``self == other`` in order to test for
        device equality.

        Parameters
        ----------
        self: Device
            device type instance. May be any supported device type.
        other: Device
            other device type instance. May be any supported device type.

        Returns
        -------
        out: bool
            a boolean indicating whether the device objects are equal.
        """
        ...
