
Typing
======

Support for ``float`` input
---------------------------

The default input type to cosmology methods is ``Array | float``. This means
that you can pass in a single float, or an array. This is useful for example
when you want to compute the angular diameter distance for a single redshift, or
for an array of redshifts. The ``float`` input is converted to an array of
length 1, and the result is returned as an array.

We document which array libraries support ``float`` inputs in the table below.
If you are using a library that does not support ``float`` inputs, you can use
the ``<array>.__array_namespace__().asarray`` function to convert your input to
an array.

.. table:: Float support in common array libraries
   :widths: auto

   =============  =========  ==============
   Array library   Version   Can add float?
   =============  =========  ==============
   NumPy          1.24.1     Yes
   Zarr           2.13.6     Yes
   Dask           2023.1.1   Yes
   Xarray         2023.2.0   Yes
   Jax            0.4.3      Yes
   Torch          1.13.1     Yes
   Tensorflow     2.11.0     Yes
   =============  =========  ==============
