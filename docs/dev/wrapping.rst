
Wrapping an Existing Library
============================

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
creating a namespace for the constants. We don't recommend building dynamic
libraries and modules and do it here only for demonstration purposes.

.. code-block:: python

    from typing import SimpleNamespace
    from example_library import some_constants, other_constants

    constants = SimpleNamespace(
        c=some_constants.speed_of_light, G=other_constants.gravitational_constant
    )
    namespace = SimpleNamespace(constants=constants)


Next we need to create a wrapper class that implements the
:class:`~cosmology.api.CosmologyWrapper` interface. Note that by the magic of
protocols we do not need to subclass anything to be considered a subclass of
:class:`~cosmology.api.CosmologyWrapper`, we just need to implement the methods.

.. code-block:: python

    @dataclass(frozen=True)
    class BaseExampleLibraryWrapper:
        cosmo: ExampleCosmology

        # ExampleCosmology does not have a name, but we can support one.
        # If we don't want to, the name can be a property that always returns None.
        name: str | None = None

        @property
        def __cosmology_namespace__(self):
            return namespace

        @property
        def constants(self):
            return self.__cosmology_namespace__.constants


To this base wrapper, we can add any other pieces that we want to support, such
as :class:`~cosmology.api.HubbleParameter`,
:class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`,
:class:`~cosmology.api.DarkEnergyComponent`,
:class:`~cosmology.api.ComovingDistanceMeasures`. Note that the Cosmology API is
built on the Array API and all outputs must be some conformant array type. A
common choice is :class:`numpy.ndarray`, but any array type that implements the
Array API will work.

.. code-block:: python

    Array: TypeAlias = np.ndarray[Any, np.floating[Any]]
    InputT: TypeAlias = Array | float


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

        # - MatterComponent -----

        @property
        def Omega_m0(self) -> Array:
            return np.array(self.cosmo.Om0)

        def Omega_m(self, z: InputT) -> Array:
            return example_library.omega_matter(self.cosmo, z)

        # - PhotonComponent -----

        @property
        def Omega_gamma0(self) -> Array:
            return np.array(self.cosmo.Ogamma0)

        def Omega_gamma(self, z: InputT) -> Array:
            return example_library.omega_photon(self.cosmo, z)

        # - DarkEnergyComponent -----

        @property
        def Omega_de0(self) -> Array:
            return np.array(self.cosmo.Ode0)

        def Omega_de(self, z: InputT) -> Array:
            return example_library.omega_lambda(self.cosmo, z)

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
a number of additional components -- all the ones that are directly releated to
the contents of ``example_library``.

Does this implement the full :class:`~cosmology.api.StandardCosmology`
interface?  No! But instances of this class can be used anywhere that only
requires the :class:`~cosmology.api.HubbleParameter`,
:class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`,
:class:`~cosmology.api.DarkEnergyComponent`, or
:class:`~cosmology.api.ComovingDistanceMeasures` methods. If functions are well
written to only require the cosmology attributes and methods that they need,
then this wrapper can be used in those functions.

.. code-block:: python

    def littleh_too_broad(cosmo: StandardCosmology):  # Not guaranteed to work!
        return cosmo.H0 / 100


    def littleh(cosmo: HasH0):  # Guaranteed to work!
        return cosmo.H0 / 100
