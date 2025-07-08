"""Test Array."""

from __future__ import annotations

import array
import sys
from enum import Enum, auto


class ArrayLibraries(Enum):
    """Array libraries."""

    array = auto()

    numpy = auto()
    zarr = auto()
    dask = auto()
    xarray = auto()

    # ML
    jax = auto()
    torch = auto()
    tensorflow = auto()


def get_array_from_library(name: ArrayLibraries) -> tuple[str, object]:  # noqa: PLR0911
    """Import an array library."""
    if name == ArrayLibraries.array:
        vrsn = "{}.{}.{}".format(*sys.version_info[:3])

        return vrsn, array.array("f", [1.0, 2.0, 3.0])

    elif name == ArrayLibraries.numpy:  # noqa: RET505
        import numpy as np  # noqa: PLC0415

        return np.__version__, np.linspace(0, 1, 10, dtype=np.float64)

    elif name == ArrayLibraries.jax:
        import jax  # noqa: PLC0415
        import jax.numpy as jnp  # noqa: PLC0415

        return jax.__version__, jnp.linspace(0, 1, 10)

    elif name == ArrayLibraries.torch:
        import torch  # noqa: PLC0415

        return torch.__version__, torch.linspace(0, 1, 10, dtype=torch.float64)

    elif name == ArrayLibraries.zarr:
        import zarr  # noqa: PLC0415

        return zarr.__version__, zarr.zeros((100, 100), chunks=(10, 10), dtype="f4")[:]

    elif name == ArrayLibraries.dask:
        import dask  # noqa: PLC0415
        import dask.array as da  # noqa: PLC0415

        return dask.__version__, da.linspace(0, 1, 10, dtype="float")

    elif name == ArrayLibraries.tensorflow:
        import tensorflow as tf  # noqa: PLC0415

        return tf.__version__, tf.linspace(0, 1, 10)

    elif name == ArrayLibraries.xarray:
        import xarray as xr  # noqa: PLC0415

        return xr.__version__, xr.DataArray([1.0, 2.0, 3.0])
    return None


if __name__ == "__main__":
    for library in ArrayLibraries:
        # import the array library
        vrsn, arr = get_array_from_library(library)

        # try adding a float
        try:
            _ = arr + 1.0
            _ = 1.0 + arr
        except Exception:  # noqa: BLE001
            print(f"{library.name}-{vrsn} failed to add a float")  # noqa: T201
        else:
            print(f"{library.name}-{vrsn} added a float")  # noqa: T201
