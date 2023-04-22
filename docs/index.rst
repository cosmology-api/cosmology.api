############################
The Cosmology API for Python
############################

The ``cosmology.api`` package provides a standard interface describing
all the pieces and the whole of a cosmology instance. This is done by defining a
collection of Protocols, which are a way to describe the interface of an object
/ class without actually implementing it. This means you can write code that
works with any object that implements the protocol, i.e many different cosmology
libraries. Cosmology libraries can conform to the the protocol without having
this library as a base class. We provide the easy-to-use, well-defined
descriptions, you can build library-agnostic functions and use them with any
supporting library. For non-conforming libraries, with the wrapper protocols as
a guide, it's easy to make a wrapper so any cosmology library can be used with
your code!

.. note::

   This package is still in development, and the API is subject to change.
   We are currently working on the release of the suite of wrapper classes
   for the most popular cosmology libraries.


.. toctree::
   :caption: Usage
   :hidden:

   install
   quickstart

.. toctree::
   :caption: API
   :hidden:

   api/typing
   api/protocols
   api/reference

.. toctree::
   :caption: Dev
   :hidden:

   dev/wrapping
   dev/new
   dev/typing

.. toctree::
   :caption: Other
   :hidden:

   changelog


Contributors
============

.. include:: ../AUTHORS.rst
