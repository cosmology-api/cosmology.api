
Typing Introduction
===================


An Introduction to Type Annotations
-----------------------------------

Since Python 3.5, the Python standard library has included the :mod:`typing`
module for annotating function and method arguments and return values with type
information. This information can be used by static type checkers such as
:mod:`mypy` to check that the code is type safe. It can also be used by IDEs to
provide type hints and even autocompletion.

A simple example of type annotations is the following function that takes two
arguments, ``x`` and ``y``, and returns their sum.

    >>> def add(x: float, y: float) -> float:
    ...     return x + y

In this example, the ``x`` and ``y`` arguments are annotated as :class:`float`
and the return value is annotated as :class:`float`. This tells the static type
checker that the function expects two :class:`float` arguments and returns a
:class:`float` value. The static type checker can then check that the function
is called with the correct types of arguments and that the return value is used
correctly. It is important to note that the type annotations are not enforced
at runtime.

Typing in Python also supports generic types, where the types of the arguments
and return value is contextual, and can be different for different calls to the
function. For example, instead of taking two :class:`float` arguments, the
``add`` function could take any two arguments of the same type and return a
value of that type.

    >>> from typing import TypeVar  # How we express generic type variable
    ...
    >>> T = TypeVar("T")  # Declare a generic type variable

    >>> def add(x: T, y: T) -> T:  # two arguments of the same type -> same return type
    ...     return x + y

    >>> add(1, 2)  # int + int -> int
    3
    ...
    >>> add(1.0, 2.0)  # float + float -> float
    3.0
    ...
    >>> add("foo", "bar")  # str + str -> str
    'foobar'


The first two examples, adding integers and floats, probably made sense to you.
The third example, adding strings, might have been a bit more surprising. But
the ``add`` function is generic, so it can be used with any type that supports
addition. If we want to make our ``add`` function only work for numerical types
such as :class:`int` and :class:`float`, we have to **constrain** the generic type
variable. The details of how to do this are beyond the scope of this
introduction, but the following example shows how to constrain the generic type
variable ``T`` to numerical types.

    >>> from typing import TypeVar
    >>> from numbers import Number
    ...
    >>> T = TypeVar("T", bound=Number)

    >>> def add(x: T, y: T) -> T:
    ...     return x + y

Now the ``add`` function can only be called with arguments that are instances or
subclasses of :class:`~numbers.Number`, like :class:`int` and :class:`float`.
But what about a :class:`~numpy.ndarray`? It is not a subclass of
:class:`~numbers.Number`, but it supports addition. To support
:class:`~numpy.ndarray` as well, we can use the :class:`typing.Union` type to
allow either :class:`~numbers.Number` or :class:`~numpy.ndarray` as arguments.

    >>> from typing import TypeVar, Union
    >>> from numbers import Number
    >>> import numpy as np
    ...
    >>> T = TypeVar("T", bound=Union[Number, np.ndarray])

    >>> def add(x: T, y: T) -> T:
    ...     return x + y

    >>> add(1, 2)
    3
    ...
    >>> add(1.0, 2.0)
    3.0
    ...
    >>> add(np.array([1, 2]), np.array([3, 4]))
    array([4, 6])


Now numpy is great, but what about a Dask array or a Jax array? They are not a
subclass of :class:`~numbers.Number` or :class:`~numpy.ndarray`, but they
support addition. We could just add them to the :class:`~typing.Union` type, but
that would be tedious and wouldn't help with Cupy or Pytorch, etc. Instead of
listing *each* types that we want to support, we can instead use the tools in
:mod:`typing` to build a generic type that describes *all* of the types that we
want to support. This is called duck-typing (or structural subtyping) and is
implemented in Python using :class:`typing.Protocol`.


An Introduction to Protocols
----------------------------

Since `PEP 544 <https://peps.python.org/pep-0544/>`_ was implemented in Python
3.8, Python can now separate the description of an API from its implementation.
This is done using the :class:`typing.Protocol` class. Protocols are essentially
abstract base classes that don't require inheritance. Instead, they are used to
describe the interface of an object. Any object that implements the interface is
considered a subclass of the Protocol and the class' instances are likewise
instances of the Protocol. This is called "structural subtyping" or "duck
typing".

As an example, consider the following Protocol that describes the interface of
an object that has a name and a value.

    >>> from typing import Protocol
    ...
    >>> class NamedValue(Protocol):
    ...     """API for Quantity."""
    ...
    ...     value: float
    ...     name: str

This Protocol can be used to annotate a function that takes a ``NamedValue``
duck-type as an argument.

    >>> def print_value(x: NamedValue) -> None:
    ...     print(f"{x.name}: {x.value}")


Any class that has a ``value`` attribute of type :class:`float` and a ``name``
attribute of type :class:`str` is considered a subclass of ``NamedValue`` and
can be used as an argument to ``print_value``.

    >>> class NamedValueClass1:
    ...     def __init__(self, name: str, value: float):
    ...         self.name = name
    ...         self.value = value
    ...
    >>> v = NamedValueClass1("foo", 1.0)
    ...
    >>> isinstance(v, NamedValue)
    True
    ...
    >>> print_value(NamedValueClass1("foo", 1.0))
    foo: 1.0

Or

    >>> from typing import NamedTuple
    ...
    >>> class NamedValueClass2(NamedTuple):
    ...     name: str
    ...     value: float
    ...
    >>> print_value(NamedValueClass2("foo", 1.0))
    foo: 1.0


Note again that neither ``NamedValueClass1`` nor ``NamedValueClass2`` inherit
from ``NamedValue``. This is the power of structural subtyping with
:class:`typing.Protocol`.

Returning to our ``add`` function, we can now use a :class:`~typing.Protocol` to
describe any of the Array libraries.

    >>> class Array(Protocol):
    ...
    ...     @property
    ...     def shape(self) -> tuple[int, ...]:
    ...         ...
    ...
    ...     @property
    ...     def dtype(self) -> Any:
    ...         ...
    ...
    ...     ...
    ...
    ...     def __add__(self, other: Array) -> Array:
    ...         ...


Applying this to our ``add`` function, we get the following.

    >>> from typing import TypeVar, Union, Protocol
    >>> from numbers import Number
    >>> import numpy as np
    ...
    >>> T = TypeVar("T", bound=Union[Number, Array])

    >>> def add(x: T, y: T) -> T:
    ...     return x + y

    >>> add(1.0, 2.0)
    3.0
    ...
    >>> add(np.array([1, 2]), np.array([3, 4]))
    array([4, 6])


The ``add`` function now works with any numerical type or any array type that
looks like ``Array``, like :class:`numpy.ndarray`, :class:`dask.array.Array`,
:class:`jax.Array`, etc.


In this Project
---------------

This API is built on the ``Array`` interface of the `Array API project
<https://data-apis.org/array-api/latest/>`_. The ``Array`` interface is not
(yet) a :class:`~typing.Protocol`, so this project privately defines a
:class:`~typing.Protocol` for ``Array``. We note that our version is a subset of
the ``Array`` interface defined by the Array API project. This is because the
Array API project is new and standard :class:`numpy.ndarray` is not yet fully
compatible, though :mod:`numpy` plans full support.

In this project you will see the ``Array`` Protocol used throughout the API.
Also, there is a generic type variable ``InputT`` that is used to describe the
type of the input to a function. This is a :class:`~typing.TypeVar`. Due to the
cuurent limitations of Python, this is an unconstrained :class:`~typing.TypeVar`
but it is intended to be constrained to ``Array`` + other, e.g. :class:`float`.
In future, ``InputT`` will be constrained.
