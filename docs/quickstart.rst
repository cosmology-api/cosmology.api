Quick Start
===========

The Cosmology API is a collection of runtime-checkable Protocols that define the
interface of a cosmology object. The Protocols can be used to describe and build
functions that work with any compatible cosmology library (and any Array
libraries that cosmology library might support), without even having a single
cosmology library as a run-time dependency.

If you didn't understand the previous paragraph, don't worry, the
:doc:`Introduction to Python Typing and Protocols </introduction>` explains the
concepts in more detail. Alternatively, we hope the examples in this Quick
Start are sufficient that you can just jump right in.


Protocol hierarchy
------------------

When you are writing a function it's important to consider what the function
needs to do and what it needs to do it. For example, a function that computes
the Hubble parameter :math:`H(z)` needs the Hubble constant :math:`H_0` and all
the component densities :math:`\Omega_{X,0}`. Other functions might need
significantly fewer attributes and methods. The Cosmology API Protocols are
designed to allow you to specify exactly what your function needs, from single
attributes and methods to fully-featured cosmology objects. We organize the
Protocols in a hierarchy, from the most general to the most specific, so you can
choose the level of detail that best suits your needs.

The cosmology protocols are grouped in levels:

* High-level :doc:`cosmology protocols </api/cosmology>` which
  describe fully-featured cosmology objects.
* Intermediate-level :doc:`component protocols </api/components>` which
  describe individual functional groups such as e.g. the physical matter and
  baryon components, or the Hubble parameters :math:`H_0` and :math:`H(z)`.
* Low-level :doc:`attribute protocols </api/attributes>` which describe the
  existence of individual methods and properties.
* Meta-level :doc:`namespace protocols </api/namespaces>` which describe the
  cosmology API itself and any API-conforming packages.


The high and intermediate-level protocols are optimally for pipelines that
perform functions requiring many attributes and methods of a Cosmology. Of
course, the protocols can also be used in simple functions. However, the
lower-level protocols allow for a more precise description of what a function
uses. For example, a function requiring only :math:`H_0` and
:math:`\Omega_{m,0}` can use the corresponding low-level protocols
:class:`~cosmology.api.HasH0` and :class:`~cosmology.api.HasOmegaM0`, instead of
the high-level, all-encompassing :class:`~cosmology.api.StandardCosmology`.

The last level, the "meta" level, is most useful for developers of cosmology
libraries and is described in the :doc:`developers section </dev/new>`.


Type Annotations
----------------

When writing a function it's often useful to specify the types of the inputs and
the outputs.  This is done using type hints.  If you are familiar with type
hints, read on; if you are unfamiliar with type hints, we recommend reading the
:doc:`previous section </introduction>` which explains the concepts in more
detail. Having agreed type hints are useful, let's look at how to use them with
the Cosmology API.

As an example, let's say we want to write a function for the Hubble parameter
:math:`H(z)` in the dark-energy-dominated era. This can be equivalently written
with the protocols at each of the hierarchy levels:

- High-level:

.. code-block:: python

    from cosmology.api import StandardCosmology  # probably everything you need


    def hubble_constant(cosmo: StandardCosmology) -> float:
        return float(np.sqrt(cosmo.Omega_de0 / 3))

- Intermediate-level:

.. code-block:: python

    from cosmology.api import DarkEnergyComponent


    def hubble_constant(cosmo: DarkEnergyComponent) -> float:
        return float(np.sqrt(cosmo.Omega_de0 / 3))

- Low-level:

.. code-block:: python

    from cosmology.api import HasOmegaDE0


    def hubble_constant(cosmo: HasOmegaDE0) -> float:
        return float(np.sqrt(cosmo.Omega_de0 / 3))


Even though the function is the same in each of the three examples, the type
annotations are different. The high-level example uses the
:class:`~cosmology.api.StandardCosmology` protocol, which describes a
fully-featured cosmology object. The intermediate-level example uses the
:class:`~cosmology.api.DarkEnergyComponent` protocol, which describes a
cosmology object with dark energy related attributes and methods. The low-level
example uses the :class:`~cosmology.api.HasOmegaDE0` protocol, which describes
an object with the attribute :attr:`~cosmology.api.HasOmegaDE0.Omega_de0`. All
three type annotations describe an object with the attribute
:attr:`~cosmology.api.HasOmegaDE0.Omega_de0`, which is why all three examples
work. However, the intermediate and high-level examples use protocols that
describe additional attributes and methods that are not required by the
function. The low-level example uses the most precise protocol that describes
only what the function needs.

If you have a type checker handy and use it on the previous examples it should
be complaining that :class:`~cosmology.api.StandardCosmology`,
:class:`~cosmology.api.DarkEnergyComponent`, and
:class:`~cosmology.api.HasOmegaDE0` are missing type hints. This is because the
Cosmology API Protocols are `generic
<https://peps.python.org/pep-0484/#generics>`_ with respect to the return types
-- of the objects attributes and methods -- and the input types of the methods.
This means that the return types and input types are not specified in the
protocol. Instead, the return types and input types are specified when the
protocol is used. The types are restricted, as the Cosmology API is built on the
`Array API <https://data-apis.org/array-api/latest/>`_ and the return types must
all be Array types.

.. note::

    Most array libraries, in particular `numpy <https://numpy.org/doc/stable/>`_
    are not yet conformant to the Array API. Many popular libraries are adopting
    the API. Currently, the Cosmology API implements an internal and stripped
    down description of the API that allows for `numpy.ndarray
    <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`_. In
    future the type will be restricted to the Array type.

    Currently the two-parameter protocols require both parameters, return and
    input type. When `PEP-696 <https://peps.python.org/pep-0696/>`_ is
    implemented, allowing for type defaults, the input type ``InputT`` will be
    defaulted to ``ReturnT | float``.


The attribute-related interfaces have only the return-type parameter.

.. skip: next
.. code-block:: python

    from typing import Protocol


    class HasOmegaDE0(Protocol[Array]):
        @property
        def Omega_de0(self) -> Array:
            ...


The method-related interfaces have both parameters.

.. skip: next
.. code-block:: python

    class HasOmegaDE(Protocol[Array, InputT]):
        def Omega_de(self, z: InputT) -> Array:
            ...


Now we can build the correct ``hubble_constant`` function, e.g. that operates on
`numpy.ndarray
<https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`_ with
`float64
<https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64>`_
dtypes.:

- Low-level:

.. code-block:: python

    from typing_extensions import TypeAlias  # Use `typing.TypeAlias` in Python 3.10+
    import numpy.typing as npt
    from numpy import float64

    Array: TypeAlias = npt.NDArray[float64]


    def hubble_constant(cosmo: HasOmegaDE0[Array]) -> Array:
        return np.sqrt(cosmo.Omega_de0 / 3)

- Intermediate-level:

.. code-block:: python

    def hubble_constant(cosmo: DarkEnergyComponent[Array, Array]) -> Array:
        return np.sqrt(cosmo.Omega_de0 / 3)

- High-level:

.. code-block:: python

    def hubble_constant(cosmo: StandardCosmology[Array, Array]) -> Array:
        return np.sqrt(cosmo.Omega_de0 / 3)


Note the :class:`~typing.TypeAlias`. We recommend using type aliases to decrease
the verbosity and increase readability of the function type hints.


Run-time Checks
---------------

The Cosmology API can also be used for runtime introspection --
:func:`isinstance` and :func:`issubclass` -- since all the protocols are
decorated with the :func:`typing.runtime_checkable` decorator.

.. warning::

    :func:`typing.runtime_checkable` allows for *structural* checks only,
    meaning :func:`isinstance` and :func:`issubclass` will only verify the
    existence of all attributes and methods, not that they have the correct
    input / output types nor the correct implementation.

.. invisible-code-block: python

    import sys
    from cosmology.api._array_api import Array

.. skip: next if(sys.version_info < (3, 10), reason="py3.10+")
.. code-block:: python

    from cosmology.api import HasOmegaDE0, HasOmegaDE


    def myfunc(cosmo: HasOmegaDE0[Array] | HasOmegaDE[Array, Array]) -> Array:
        if isinstance(cosmo, HasOmegaDE0):
            return cosmo.Omega_de0
        elif isinstance(cosmo, HasOmegaDE):
            return cosmo.Omega_de(0)


Next Steps
----------

The :doc:`Protocols </api/protocols>` allow you to specify and inspect which
attributes are supported by a given cosmology object.

The :doc:`reference </api/reference>` provides a flat
list of all attributes which can potentially be supported by cosmology
instances.
