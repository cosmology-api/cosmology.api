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


Type Annotations
----------------

When writing a function it's often useful to specify the types of the inputs and
the outputs.  This is done using type hints.  If you are familiar with type
hints, read on; if you are unfamiliar with type hints, we recommend reading the
:doc:`introduction </introduction>`, which explains the concepts in more
detail. Having agreed type hints are useful, let's look at how to use them with
the Cosmology API.

As an example, let's say we want to write a function that computes :math:`S_8 =
\sigma_8 \, \sqrt{\Omega_{m,0}/0.3}` as a function of :math:`\sigma_8`, with
:math:`\Omega_{m,0}` coming from the current cosmology.  Using the Cosmology
API, such a function can be annotated as:

.. code-block:: python

    from cosmology.api import HasOmegaM0


    def S_8(sigma_8: float, cosmo: HasOmegaM0) -> float:
        return sigma_8 * (cosmo.Omega_m0 / 0.3) ** 0.5

Here, the annotation with the :class:`~cosmology.api.HasOmegaM0` protocol
declares that the ``cosmo`` object must have an attribute
:attr:`~cosmology.api.HasOmegaM0.Omega_m0`, which is subsequently used by the
function.

If you have a type checker handy, and use it on the previous example, it might
complain that :class:`~cosmology.api.HasOmegaM0` is missing a type hint. This
is because the Cosmology API Protocols are `generic
<https://typing.readthedocs.io/en/latest/reference/generics.html>`_ with
respect to the types of its attributes and methods.  This means that the return
types and input types are not specified in the protocol. Instead, the return
types and input types are specified when the protocol is used. The types are
restricted, as the Cosmology API is built on the `Array API
<https://data-apis.org/array-api/latest/>`_ and the return types must all be
Array types.

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


    class HasOmegaM0(Protocol[Array]):
        @property
        def Omega_m0(self) -> Array: ...


The method-related interfaces have both parameters.

.. skip: next
.. code-block:: python

    class HasOmegaM(Protocol[Array, InputT]):
        def Omega_m(self, z: InputT) -> Array: ...


We can hence a working function that expects :math:`\Omega_{m,0}` to be a plain
Python ``float``:

.. code-block:: python

    from cosmology.api import HasOmegaM0


    def S_8(sigma_8: float, cosmo: HasOmegaM0[float]) -> float:
        return sigma_8 * (cosmo.Omega_m0 / 0.3) ** 0.5

And this should now type-check successfully.


Combining Protocols
-------------------

When you are writing a function it's important to consider what the function
needs to do and what it needs to do it. For example, a function that computes
the Hubble parameter :math:`H(z)` needs the Hubble constant :math:`H_0` and all
the component densities :math:`\Omega_{X,0}`. Other functions might need
significantly fewer attributes and methods. The Cosmology API defines a set of
:doc:`Protocols </api/protocols>` that are designed to allow you to specify
exactly what your code needs, by combining multiple protocols into your own
bespoke Cosmology interface:

.. code-block:: python

    from typing import Any, Protocol
    from numpy.typing import NDArray
    from cosmology.api import HasComovingDistance, HasH0

    # my code is working with NumPy arrays
    Array = NDArray[Any]


    # the cosmology interface for my code
    class Cosmology(
        HasComovingDistance[Array, Array],
        HasH0[Array],
        Protocol,
    ): ...


    # my code uses my cosmology interface
    def my_function(z: Array, cosmo: Cosmology) -> Array:
        """Do my computation using my Cosmology interface."""
        ...

This mix-and-match approach allows you to describe the minimal set of methods
and attributes that a cosmology code needs to support for your code.  It also
means your code will work with any Cosmology API-compliant library as soon as
it supports the features you need, even if it doesn't support some other
features that the API describes.


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

The :doc:`reference </api/reference>` provides a flat list of all attributes
which can potentially be supported by cosmology instances.
