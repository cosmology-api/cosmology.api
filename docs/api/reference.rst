Reference
=========

.. currentmodule:: cosmology.api

This page contains a list of all methods and attributes that a Cosmology
instance might support.

Each item on this list is described in an associated :doc:`protocol
</api/protocols>`.


Hubble parameter
----------------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasH.H
   ~HasH0.H0
   ~HasHoverH0.H_over_H0
   ~HasScaleFactor.scale_factor
   ~HasScaleFactor0.scale_factor0


Distance
--------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasAngularDiameterDistance.angular_diameter_distance
   ~HasComovingDistance.comoving_distance
   ~HasHubbleDistance.hubble_distance
   ~HasLookbackDistance.lookback_distance
   ~HasLuminosityDistance.luminosity_distance
   ~HasProperDistance.proper_distance
   ~HasTransverseComovingDistance.transverse_comoving_distance


Volume
------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasComovingVolume.comoving_volume
   ~HasDifferentialComovingVolume.differential_comoving_volume


Time
----

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasAge.age
   ~HasHubbleTime.hubble_time
   ~HasProperTime.proper_time
   ~HasLookbackTime.lookback_time


Density
-------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasOmegaTot.Omega_tot
   ~HasOmegaTot0.Omega_tot0
   ~HasCriticalDensity.critical_density
   ~HasCriticalDensity0.critical_density0


Matter
------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasOmegaB.Omega_b
   ~HasOmegaB0.Omega_b0
   ~HasOmegaDM.Omega_dm
   ~HasOmegaDM0.Omega_dm0
   ~HasOmegaM.Omega_m
   ~HasOmegaM0.Omega_m0


Dark energy
-----------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasOmegaDE.Omega_de
   ~HasOmegaDE0.Omega_de0


Radiation
---------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasOmegaGamma.Omega_gamma
   ~HasOmegaGamma0.Omega_gamma0


Neutrinos
---------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasNeff.Neff
   ~HasOmegaNu.Omega_nu
   ~HasOmegaNu0.Omega_nu0
   ~HasMNu.m_nu


Curvature
---------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasOmegaK.Omega_k
   ~HasOmegaK0.Omega_k0


Cosmic microwave background
---------------------------

.. autosummary::
   :toctree: reference
   :template: reference

   ~HasTCMB.T_cmb
   ~HasTCMB0.T_cmb0
