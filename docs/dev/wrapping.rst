
Wrapping an Existing Library
============================

If you have an existing library that you would like to wrap, the Cosmology API
is designed to be as simple as possible.  Essentially, you need to create an
object that implements the :class:`cosmology.api.CosmologyWrapper` interface, as
well any other pieces (e.g. :class:`cosmology.api.DistanceMeasures`) that you
want to support and map the methods to the appropriate functions on your
cosmology object / in your library.

Let's work through an example.  Suppose you have a library that provides a
:class:`Cosmology` class that only has the cosmological parameters and the rest
of the cosmological calculations are done by functions in the library. The library
also has some constants, such as the speed of light, that are used in the
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
            - comoving_distance()
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


Now let's wrap this library.  First, we need to create a wrapping of the library
so that it implements the :class:`cosmology.api.CosmologyNamespace` interface.


.. code-block:: python

    from typing import SimpleNamespace
    from example_library import some_constants, other_constants

    constants = SimpleNamespace(
        c=some_constants.speed_of_light, G=other_constants.gravitational_constant
    )
    namespace = SimpleNamespace(constants=constants)


Next we need to create a wrapper class that implements the
:class:`cosmology.api.CosmologyWrapper` interface. Note that we do not need to
subclass anything, we just need to implement the methods.

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

        ...


To this base wrapper, we can add any other pieces that we want to support, such
as :class:`~cosmology.api.HubbleParameter`,
:class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`,
:class:`~cosmology.api.DarkEnergyComponent`,
:class:`~cosmology.api.ComovingDistanceMeasures`. Note that the Cosmology API is
built on the Array API and all outputs must be some conformant array type.

.. code-block:: python

    class ExampleLibraryWrapper(BaseExampleLibraryWrapper):
        # - HubbleParameter -----

        @property
        def H0(self) -> ndarray:
            return np.array(self.cosmo.H0)

        def H(self, z: np.ndarray | float) -> np.ndarray:
            return example_library.hubble_parameter(self.cosmo, z)

        @property
        def hubble_distance(self) -> np.ndarray:
            return np.array(self.constants.c / self.H0 * converstion_to_Mpc)

        @property
        def hubble_time(self) -> np.ndarray:
            return np.array(1 / self.H0 * converstion_to_Gyr)

        # - MatterComponent -----

        @property
        def Omega_m0(self) -> np.ndarray:
            return np.array(self.cosmo.Om0)

        def Omega_m(self, z: np.ndarray | float) -> np.ndarray:
            return example_library.omega_matter(self.cosmo, z)

        # - PhotonComponent -----

        @property
        def Omega_gamma0(self) -> np.ndarray:
            return np.array(self.cosmo.Ogamma0)

        def Omega_gamma(self, z: np.ndarray | float) -> np.ndarray:
            return example_library.omega_photon(self.cosmo, z)

        # - DarkEnergyComponent -----

        @property
        def Omega_de0(self) -> np.ndarray:
            return np.array(self.cosmo.Ode0)

        def Omega_de(self, z: np.ndarray | float) -> np.ndarray:
            return example_library.omega_lambda(self.cosmo, z)

        # - ComovingDistanceMeasures -----

        def comoving_distance(self, z: np.ndarray | float) -> np.ndarray:
            return example_library.comoving_distance(self.cosmo, z)

        def transverse_comoving_distance(self, z: np.ndarray | float) -> np.ndarray:
            return ...  # up to you to implement this

        def comoving_volume(self, z: np.ndarray | float) -> np.ndarray:
            return ...  # up to you to implement this

        def differential_comoving_volume(self, z: np.ndarray | float) -> np.ndarray:
            return ...  # up to you to implement this


Great! Now we have a wrapper that implements the base Cosmology API and supports
a number of additional components -- all the ones that are directly releated to the contents of ``example_library``.

Does this implement the full :class:`~cosmology.api.StandardCosmology`
interface?  No! But this class can still be used anywhere that only requires the
:class:`~cosmology.api.HubbleParameter`,
:class:`~cosmology.api.MatterComponent`,
:class:`~cosmology.api.PhotonComponent`,
:class:`~cosmology.api.DarkEnergyComponent`, or
:class:`~cosmology.api.ComovingDistanceMeasures` methods. If functions are well
written to only require the cosmology attributes and methods that they need,
then this wrapper can be used in those functions.
