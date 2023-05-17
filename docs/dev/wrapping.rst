
Wrapping an Existing Library
============================

.. invisible-code-block: python

    import sys

Many cosmology libraries already exist, such as ``astropy.cosmology``,
``CLASS``, and ``CAMB``, and all have different inerfaces that are not
compatible with each other.  The Cosmology API is designed to be a common
interface and we can easily wrap existing codes to make them compatible with the
Cosmology API.  Many of the common cosmology libraries are already wrapped and
available in the `cosmology.compat
<https://github.com/cosmology-api/cosmology-compat>`_ module.


If there is an unsopported library that you would like to wrap, the Cosmology
API is designed to be as simple as possible.  Essentially, you need to create an
object that implements the :class:`cosmology.api.CosmologyWrapper` interface, as
well any other pieces (e.g. :class:`cosmology.api.DistanceMeasures`) that you
want to support and map the methods to the appropriate functions on the
cosmology object / in the library.

Let's work through an example.  Suppose you have a library that provides a
:class:`Cosmology` class that only has the cosmological parameters and the rest
of the cosmological calculations are done by functions in the library. The
library also has some constants, such as the speed of light, that are used in
calculations.  The library looks something like this:

.. code-block::

    example_library/
        __init__.py
        some_constants.py
           - speed_of_light
        other_constants.py
           - gravitational constant
        cosmology_class.py
            - ExampleCosmology
        functions.py
            - comoving_distance_z1z2()
            - hubble_parameter()
            - omega_matter()
            - omega_photon()
            - omega_lambda()

The cosmology class looks something like this:

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class ExampleCosmology:
        H0: float
        Om0: float
        Ogamma0: float
        Ode0: float


Now let's wrap this library.  First, we need to create a wrapping of the
top-level namespace so that it implements the
:class:`cosmology.api.CosmologyNamespace` interface. This will also require
creating a namespace for the constants.

.. skip: next
.. code-block:: python

    # wrapper/__init__.py
    from . import constants

    ...


.. skip: next
.. code-block:: python

    # wrapper/constants.py
    from example_library import some_constants, other_constants

    c = some_constants.speed_of_light
    G = other_constants.gravitational_constant


Next we need to create a wrapper class that implements the
:class:`~cosmology.api.CosmologyWrapper` interface. Note that by the magic of
protocols we do not need to subclass anything to be considered a subclass of
:class:`~cosmology.api.CosmologyWrapper`, we just need to implement the methods.

.. skip: next
.. code-block:: python

    import wrapper


    @dataclass(frozen=True)
    class BaseExampleLibraryWrapper:
        cosmo: ExampleCosmology

        # ExampleCosmology does not have a name, but we can support one.
        # If we don't want to, the name can be a property that always returns None.
        name: str | None = None

        @property
        def __cosmology_namespace__(self):
            return wrapper

        @property
        def constants(self):
            return self.__cosmology_namespace__.constants


.. skip: next if(sys.version_info < (3, 10), reason="py310+")
.. invisible-code-block: python

    from types import SimpleNamespace
    from cosmology.api import CosmologyNamespace, CosmologyConstantsNamespace

    constants = SimpleNamespace(G=1, c=2)
    library = SimpleNamespace(constants=constants)

    @dataclass(frozen=True)
    class BaseExampleLibraryWrapper:
        cosmo: ExampleCosmology
        name: str | None = None

        @property
        def __cosmology_namespace__(self):
            return library

        @property
        def constants(self):
            return self.__cosmology_namespace__.constants


To this base wrapper, we can add any other pieces that we want to support, such
as :class:`~cosmology.api.HubbleParameter`,
:class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`,
:class:`~cosmology.api.DarkEnergyComponent`, and
:class:`~cosmology.api.ComovingDistanceMeasures`. Note that the Cosmology API is
built on the Array API and all outputs must be some conformant array type. A
common choice is :class:`numpy.ndarray`, but any array type that implements the
Array API will work. For this example we will add support for
:class:`~cosmology.api.HubbleParameter` and
:class:`~cosmology.api.ComovingDistanceMeasures`.

.. skip: next if(sys.version_info < (3, 10), reason="py310+")
.. code-block:: python

    from typing import Any, Union
    from typing_extensions import TypeAlias
    import numpy as np

    Array: TypeAlias = np.ndarray[Any, np.floating[Any]]
    InputT: TypeAlias = Union[Array, float]


    class ExampleLibraryWrapper(BaseExampleLibraryWrapper):
        # - HubbleParameter -----

        @property
        def H0(self) -> Array:
            return np.array(self.cosmo.H0)

        def H(self, z: InputT) -> Array:
            return example_library.hubble_parameter(self.cosmo, z)

        @property
        def hubble_distance(self) -> Array:
            return np.array(self.constants.c / self.H0 * converstion_to_Mpc)

        @property
        def hubble_time(self) -> Array:
            return np.array(1 / self.H0 * converstion_to_Gyr)

        # - ComovingDistanceMeasures -----

        def comoving_distance(self, z1: InputT, z2: InputT | None = None) -> Array:
            z1, z2 = (z1, z2) if z2 is not None else (0, z1)
            return example_library.comoving_distance_z1z2(self.cosmo, z1, z2)

        def transverse_comoving_distance(
            self, z1: InputT, z2: InputT | None = None
        ) -> Array:
            ...  # up to you to implement this

        def comoving_volume(self, z1: InputT, z2: InputT | None = None) -> Array:
            ...  # up to you to implement this

        def differential_comoving_volume(
            self, z1: InputT, z2: InputT | None = None
        ) -> Array:
            ...  # up to you to implement this


Great! Now we have a wrapper that implements the base Cosmology API and supports
a number of additional components -- though not yet all the ones that are in
``example_library``.

Does this implement the full :class:`~cosmology.api.StandardCosmology`
interface?  No! But instances of this class can be used anywhere that only
requires the :class:`~cosmology.api.HubbleParameter` or
:class:`~cosmology.api.ComovingDistanceMeasures` methods. If functions are well
written to only require the cosmology attributes and methods that they need,
then this wrapper can be used in those functions.

.. code-block:: python

    from cosmology.api import HasH0, StandardCosmology


    def littleh_too_broad(cosmo: StandardCosmology):  # Not guaranteed to work!
        return cosmo.H0 / 100


    def littleh(cosmo: HasH0):  # Guaranteed to work!
        return cosmo.H0 / 100


To keep things simple the above ``ExampleLibraryWrapper`` only implemented the
:class:`~cosmology.api.HubbleParameter` and
:class:`~cosmology.api.ComovingDistanceMeasures` methods. However, the
``example_library`` also has a number of other components that we can add to our
wrapper: :class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`, and
:class:`~cosmology.api.DarkEnergyComponent`. We could go back and add these to
the ``ExampleLibraryWrapper`` class, or we can create a new wrapper that
inherits from ``ExampleLibraryWrapper`` and adds the additional components,
whatever is most convenient for your use case. For this example we will create a
"mixin" class for :class:`~cosmology.api.MatterComponent` that may be used in
either scenario.

.. skip: next if(sys.version_info < (3, 10), reason="py310+")
.. code-block:: python

    class MatterMixin:
        cosmo: ExampleCosmology

        @property
        def Omega_m0(self) -> Array:
            return np.array(self.cosmo.Om0)

        def Omega_m(self, z: InputT) -> Array:
            return example_library.omega_matter(self.cosmo, z)


The point is that ``ExampleLibraryWrapper`` can be extended to support as much
or as little of the Cosmology API as is needed. Though it would be nice if
functions were written to only require the cosmology attributes and methods that
they need, it is expected that many functions are too broadly typed e.g.
``littleh_too_broad`` above. Consequently, if the wrapper can support the full
:class:`~cosmology.api.StandardCosmology` it is recommended to do so. However,
if only a subset of the API is possible, then it is better to implement that
subset than to not.
