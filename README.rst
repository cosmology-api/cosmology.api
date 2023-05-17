Cosmology API
=============

There are a lot of (Python) cosmology libraries out there, from big projects --
including `Astropy <https://docs.astropy.org/en/stable/cosmology/index.html>`_,
`CLASS <http://class-code.net>`_, and `CAMB
<https://camb.readthedocs.io/en/latest/>`_ -- down to small personal scripts.
These libraries perform many of the same tasks, but they all have different
interfaces, and different ways of doing things. This makes it hard to switch
between libraries, and nearly impossible to write code that works with multiple
libraries.

The Cosmology API for Python solves this problem, providing detailed interfaces
for cosmology codes, from individual methods and functions up to fully-featured
cosmology objects, even whole libraries. Best of all, using the Cosmology API
does not require any run-time dependencies, even this library!

With the Cosmology API you can **write code that works with anything that
implements the API**, i.e many different cosmology libraries. We provide the
easy-to-use, well-defined descriptions, you can build functions that work with
any supporting library. For example

.. skip: next
.. code-block:: python

   # No implementation, just a description of the interface!
   from cosmology.api import StandardCosmology


   def flat_angular_diameter_distance(
       cosmo: StandardCosmology[Array, Array], z: Array
   ) -> Array:
       # Do some cosmology with any object that implements the API
       if cosmo.Omega_k != 0:
           raise ValueError("This function only works for flat cosmologies")
       return cosmo.comoving_distance(z) / (1 + z)
