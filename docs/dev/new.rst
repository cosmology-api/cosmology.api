
Building a Conformant Library
=============================

There are two pieces to building a conformant library:

1. Having a cosmology class that conforms to the Cosmology API
2. Implementing the required set of modules in the library

Let's start with the 2nd requirement, which is the easier of the two.

.. warning::

    Remember that run-time checks of protocols only validate the existence of
    attributes and methods, not important details like their input and output
    types. For more detailed checks it is necessary to inspect the signatures of
    the methods and attributes.


Library Layout
--------------

At present, the library layout is very simple. All that is required is that the
library must have a top-level module called "constants".

.. code-block:: text

    library/

        constants.py


The :doc:`Cosmology-API <../index>` package provides two run-time checkable
Protocols that can be used for static and run-time checks that the library and the
constants module conform to the API. See the protocols for details.

- :class:`~cosmology.api.CosmologyConstantsNamespace`
- :class:`~cosmology.constants.CosmologyConstantsNamespace`)


Cosmology Classes
-----------------

The second part to a conformant library is to have a cosmology class that
conforms to the Cosmology API. This is a bit more involved, but not too bad. The
:doc:`Cosmology-API <../index>` package provides many protocols for the various
methods and attributes of the Cosmology API. These protocols can be used as
abstract base classes, or only as reference, or both. By the magic of protocols,
inheritance from the protocols is not required for the cosmology class and its
instances to be considered subclasses and instances of the protocol!

As an example, let's look at the base :class:`~cosmology.api.Cosmology` protocol.

    >>> from dataclasses import dataclass

    >>> @dataclass
    >>> class MyCosmology:  # NOT a subclass of Cosmology!
    ...     name: str | None
    ...
    ...     @property
    ...     def __cosmology_namespace__(self):
    ...         return None  # Technically incorrect, see above warning.
    ...
    ...    @property
    ...    def constants(self):
    ...        return None  # Technically incorrect, see above warning.

    >>> from cosmology.api import Cosmology
    >>> isinstance(MyCosmology, Cosmology)
    True


The above example is also a good introduction to the
:class:`~cosmology.api.Cosmology` API. Cosmology classes must have a ``name``,
which should be a human-friendly label of the cosmology, for example ``"Planck
2018"`` when working with a FLRW-like cosmology with the Planck 2018 parameters.
Cosmology classes must also have a ``__cosmology_namespace__`` attribute, which
is a :class:`~cosmology.api.CosmologyNamespace` instance. This allows us to
access the package from which a cosmology instance was defined. As a convenience
for users, the cosmology class should also have a ``constants`` attribute, which
is a :class:`~cosmology.api.CosmologyConstantsNamespace`, which allows users to
see the constants used by the cosmology. Normally the ``constants`` attribute
just returns ``self.__cosmology_namespace__.constants``, but this is not a
strict requirement, allowing for more flexibility in the implementation such as
implementing different constants.

The following example shows more correct outputs to the
``__cosmology_namespace__`` and ``constants`` attributes. We don't recommend
building dynamic libraries and modules and do it here only for demonstration
purposes.

    >>> from typing import SimpleNamespace
    >>> from cosmology.api import CosmologyNamespace, CosmologyConstantsNamespace

    >>> constants = SimpleNamespace(G=1, c=2)
    >>> library = SimpleNamespace(constants=constants)

    >>> @dataclass
    >>> class MyCosmology:  # NOT a subclass of Cosmology!
    ...     name: str | None
    ...
    ...     @property
    ...     def __cosmology_namespace__(self) -> CosmologyNamespace:
    ...         return library
    ...
    ...    @property
    ...    def constants(self) -> CosmologyConstantsNamespace:
    ...        return self.__cosmology_namespace__.constants

    >>> isinstance(MyCosmology.__cosmology_namespace__, CosmologyNamespace)
    True
    >>> isinstance(MyCosmology.constants, CosmologyConstantsNamespace)
    True
