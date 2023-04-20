
Typing
======

[Introduction about typing support in the cosmology protocols.]

If you do not require static or dynamic type checking of cosmology instances,
the :doc:`reference </api/reference>` provides a flat list of all methods and
properties that a cosmology instance can support.


Generic cosmology types
-----------------------

[Introduction about generic cosmology types, including the ``Array`` and
``InputT`` type variables.]


Support for ``float`` input
---------------------------

[Introduction about accepting ``float`` input to the cosmology methods.]

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
