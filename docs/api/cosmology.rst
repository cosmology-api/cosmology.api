
Cosmology
=========

.. currentmodule:: cosmology.api

This page lists the high-level cosmology protocol.  This is a fully-featured
interface to describe the cosmological background of a physical universe.

At a lower level of abstraction, a cosmology consists of individual
:doc:`components </api/components>`.

.. autoclass:: Cosmology()
   :special-members:

   .. autoproperty:: __cosmology_namespace__
   .. autoproperty:: constants
   .. autoproperty:: name

.. autoclass:: StandardCosmology()
   :special-members:

   .. autoproperty:: __cosmology_namespace__
   .. autoproperty:: constants
   .. autoproperty:: name


Wrappers
========

In order to provide a consistent interface, existing cosmology libraries can be
wrapped to conform to the :doc:`Cosmology-API <../index>`.  The form of these
wrappers is specified here.

Details of using these wrappers is upcoming. You can see the development of the Astropy and CAMB wrappers in the ``cosmology-api`` github repo.

For details of how to write your own wrapper, see the :doc:`developer documentation <../dev/wrapping>`.

.. currentmodule:: cosmology.api.compat

.. autoclass:: CosmologyWrapper()
   :special-members:


.. autoclass:: StandardCosmologyWrapper()
   :special-members:
