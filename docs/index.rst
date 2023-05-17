############################
The Cosmology API for Python
############################

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
       if cosmo.Omega_k0 != 0:
           raise ValueError("This function only works for flat cosmologies")
       return cosmo.comoving_distance(z) / (1 + z)


.. note::

   This package is still in development, and the API is subject to change.
   We are currently working on the release of the suite of wrapper classes
   for the most popular cosmology libraries.


There are a few types of people who might find themselves reading this:

1. **End users** who want to do some cosmology with an existing library and
   aren't planning on sharing their analysis scripts for re-use. Welcome, but
   you probably don't need to read this documentation. Just check that your
   preferred library implements the API, and you're good to go.

2. **End users** who want to write code that works with multiple cosmology
   libraries. Welcome, the docs are layed out primarily with you in mind! You
   should start with the Usage section of this documentation, and then read and
   use the API section when writing your code. If you encounter and need some
   code that doesn't implement this API, please read the Developers section or
   contact the developers of that library and point them to use case #3.

3. **Library developers** who want to make their library compatible with the
   Cosmology API. Welcome, we're glad you're here! In addition to the Usage and
   API sections, we have the Developers section of this documentation with you
   in mind.


.. toctree::
   :caption: Usage
   :hidden:

   install
   introduction
   quickstart

.. toctree::
   :caption: API
   :hidden:

   api/protocols
   api/reference

.. toctree::
   :caption: Developers
   :hidden:

   dev/wrapping
   dev/new
   dev/types

.. toctree::
   :caption: Other
   :hidden:

   changelog


Contributors
============

.. include:: ../AUTHORS.rst
