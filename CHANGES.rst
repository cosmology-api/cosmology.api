Changelog (``cosmology.api``)
=============================

0.1.0 (unreleased)
------------------

- ``CosmologyNamespace`` is the Protocol defining the main namespace of the API. (#1) [@nstarman]
    - Added ``constants`` is the constants namespace. (#1) [@nstarman]
    - Rename ``CosmologyAPINamespace`` to ``CosmologyNamespace`` (#40) [@nstarman]


- ``CosmologyConstantsNamespace`` is the Protocol defining the constants namespace of the API. (#1) [@nstarman]
    - Rename ``CosmologyConstantsAPINamespace`` to ``CosmologyConstantsNamespace`` (#40) [@nstarman]

  Attributes:
    - Added ``G`` is the gravitational constant. (#1) [@nstarman]
    - Added ``c`` to the constants namespace. (#11) [@nstarman]
        - Renamed ``speed_of_light`` to ``c``. (#19) [@nstarman]

- ``Cosmology`` is the Protocol defining conformant cosmology classes.
    - Renamed ``CosmologyAPIConformant`` to ``CosmologyAPI``. (#16) [@nstarman]
    - Renamed ``CosmologyAPI`` to ``Cosmology``. (#40) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]

  Attributes:
    - ``__cosmology_namespace__``  (#1) [@nstarman]
        - Simplified to an attribute (#46) [@nstarman]
    - ``name``, the name of the cosmology instance  (#1) [@nstarman]
    - ``constants`` is the constants namespace. (#45) [@nstarman]


- ``StandardCosmology`` is the Protocol defining conformant FLRW cosmology classes.
    - All attributes and methods are read-only. (#13) [@nstarman]
    - Renamed ``FLRWAPIConformant`` to ``FLRWCosmologyAPI``. (#16) [@nstarman]
    - Split into ``FLRWCosmologyAPI`` and ``StandardFLRWCosmologyAPI``. (#18) [@nstarman]
    - Renamed ``FLRWCosmologyAPI`` to ``BackgroundCosmologyAPI`` and
      ``StandardFLRWCosmologyAPI`` to ``StandardCosmologyAPI``. (#19)
      [@nstarman]
    - Break the standard cosmology into a composition of components (#25) [@nstarman]
    - Renamed ``StandardCosmologyAPI`` to ``StandardCosmologyAPI`` (#39) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``Cosmology``, ``BaryonComponent``,  ``CurvatureComponent``, ``DarkEnergyComponent``, ``DarkMatterComponent``, ``MatterComponent``, ``NeutrinoComponent``, ``PhotonComponent``, ``TotalComponent``, ``DistanceMeasures``, ``HubbleParameter``, ``CriticalDensity`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_tot0`` - removed
    - ``rho_tot`` - removed

- ``CosmologyWrapper`` is the Protocol defining an API-conformant wrapper for a non-conformant cosmology class. (#5) [@nstarman]
    - A default implementation is provided for ``__getattr__`` that passes
      through to the wrapped object. (#8) [@nstarman]
    - Renamed ``CosmologyAPIConformantWrapper`` to ``CosmologyWrapper``. (#16) [@nstarman]
    - Renamed ``CosmologyWrapper`` to ``CosmologyWrapperAPI`` and back. (#17, #40) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]

- ``StandardCosmologyWrapper`` is the Protocol defining an API-conformant wrapper for a non-conformant FLRW cosmology class. (#5) [@nstarman]
    - A default implementation is provided for ``__getattr__`` that passes
      through to the wrapped object. (#8) [@nstarman]
    - Renamed ``FLRWAPIConformantWrapper`` to ``FLRWCosmologyWrapper``. (#16) [@nstarman]
    - Renamed ``FLRWCosmologyWrapper`` to ``FLRWCosmologyWrapperAPI``. (#17) [@nstarman]
    - Split into ``FLRWCosmologyWrapperAPI`` and ``StandardFLRWCosmologyWrapperAPI``. (#18) [@nstarman]
    - Renamed ``FLRWCosmologyWrapperAPI`` to ``BackgroundCosmologyWrapperAPI`` and
      ``StandardFLRWCosmologyWrapperAPI`` to ``StandardCosmologyWrapperAPI``. (#19)
      [@nstarman]
    - Renamed to ``StandardCosmologyWrapper`` (#40) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]


- ``HasOmegaM0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_m0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Om0`` to ``Omega_m0`` (#37) [@nstarman]

- ``HasOmegaM`` (#48) [@nstarman, @@ntessore]
    - ``Omega_m`` - moved here (#25, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Om`` to ``Omega_m`` (#37) [@nstarman]

- ``MatterComponent``  (#25) [@nstarman]
    - Renamed ``MatterComponent`` to ``HasMatterComponent`` and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaM0``, ``HasOmegaM`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_m0`` - removed (#19) [@nstarman]
    - ``rho_m`` - removed (#19) [@nstarman]


- ``HasOmegaB0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_b0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Ob`` to ``Omega_b0`` (#37) [@nstarman]

- ``HasOmegaB`` (#48) [@nstarman, @@ntessore]
    - ``Omega_b`` - moved here (#25, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Ob`` to ``Omega_b`` (#37) [@nstarman]

- ``BaryonComponent``  (#25) [@nstarman]
    - Renamed ``BaryonComponent`` to ``HasBaryonComponent`` and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaB0``, ``HasOmegaB`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_b0`` - removed (#19) [@nstarman]
    - ``rho_b`` - removed (#19) [@nstarman]


- ``HasOmegaDM0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_dm0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Odm0`` to ``Omega_dm0`` (#37) [@nstarman]

- ``HasOmegaDM`` (#48) [@nstarman, @@ntessore]
    - ``Omega_dm`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Odm`` to ``Omega_dm`` (#37) [@nstarman]

- ``DarkMatterComponent``  (#25) [@nstarman]
    - Renamed ``DarkMatterComponent`` to ``HasDarkMatterComponent`` and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaDM0``, ``HasOmegaM`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_dm0`` - removed (#19) [@nstarman]
    - ``rho_dm`` - removed (#19) [@nstarman]


- ``HasOmegaDE0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_de0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Ode0`` to ``Omega_de0`` (#37) [@nstarman]

- ``HasOmegaDE`` (#48) [@nstarman, @@ntessore]
    - ``Omega_de`` - moved here (#25) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Ode`` to ``Omega_de`` (#37) [@nstarman]

- ``DarkEnergyComponent``  (#25) [@nstarman]
    - Renamed ``DarkEnergyComponent`` to ``HasDarkEnergyComponent`` and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaDE0``, ``HasOmegaDE`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_de0`` - removed (#19) [@nstarman]
    - ``rho_de`` - removed (#19) [@nstarman]


- ``HasOmegaK0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_k0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Ok0`` to ``Omega_k0`` (#37) [@nstarman]

- ``HasOmegaK`` (#48) [@nstarman, @@ntessore]
    - ``Omega_k`` - moved here (#25, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Ok`` to ``Omega_k`` (#37) [@nstarman]

- ``CurvatureComponent``  (#25) [@nstarman]
    - Renamed ``GlobalCurvatureComponent`` to ``HasGlobalCurvatureComponent``. (#33) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaK0``, ``HasOmegaK`` (#48) [@nstarman, @@ntessore]
    - Renamed ``GlobalCurvatureComponent`` to ``CurvatureComponent``. (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_k0`` - removed (#19) [@nstarman]
    - ``rho_k`` - removed (#19) [@nstarman]


- ``HasOmegaGamma0`` (#48) [@nstarman, @@ntessore]
    - ``Ogamma0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Ogamma0`` to ``Omega_gamma0`` (#37) [@nstarman]

- ``HasOmegaGamma`` (#48) [@nstarman, @@ntessore]
    - ``Omega_gamma`` - moved here (#25, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Ogamma`` to ``Omega_gamma`` (#37) [@nstarman]

- ``PhotonComponent``  (#25) [@nstarman]
    - Renamed ``PhotonComponent`` to ``HasPhotonComponent``, and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOgamma0``, ``HasOgamma`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_gamma0`` - removed (#19) [@nstarman]
    - ``rho_gamma`` - removed (#19) [@nstarman]


- ``HasOmegaNu0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_nu0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Onu0`` to ``Omega_nu0`` (#37) [@nstarman]

- ``HasNeff`` (#48) [@nstarman, @@ntessore]
    - ``Neff`` - moved here (#25, #48) [@nstarman]

- ``HasMNu`` (#48) [@nstarman, @@ntessore]
    - ``m_nu`` - tuple of neutrino masses in eV (#1, #12, #25) [@nstarman]

- ``HasOmegaNu`` (#48) [@nstarman, @@ntessore]
    - ``Omega_nu`` - moved here (#25, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Onu`` to ``Omega_nu`` (#37) [@nstarman]

- ``NeutrinoComponent``  (#25) [@nstarman]
    - Renamed ``NeutrinoComponent`` to ``HasNeutrinoComponent``, and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasOmegaNu0``, ``HasNeff``, ``HasMNu``, ``HasOmegaNu`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``rho_nu0`` - removed (#19) [@nstarman]
    - ``rho_nu`` - removed (#19) [@nstarman]


- ``HasOmegaTot0`` (#48) [@nstarman, @@ntessore]
    - ``Omega_tot0``
        - Renamed ``Otot0`` to ``Omega_tot0`` (#37) [@nstarman]

- ``HasOmegaTot`` (#48) [@nstarman, @@ntessore]
    - ``Omega_tot``
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Otot`` to ``Omega_tot`` (#37) [@nstarman]

- ``TotalComponent`` (#38) [@nstarman]
    - Split from ``StandardCosmology``. (#38) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Renamed ``HasTotalComponent`` to ``TotalComponent``. (#48) [@nstarman, @@ntessore]
    - Subclass of ``HasOmegaTot0`` and ``HasOmegaTot`` (#48) [@nstarman, @@ntessore]


- ``HasH0`` (#48) [@nstarman, @@ntessore]
    - ``H0`` - moved here (#31, #48) [@nstarman]

- ``HasH`` (#48) [@nstarman, @@ntessore]
    - ``H`` - moved here (#31, #48) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]

- ``HasHubbleDistance`` (#48) [@nstarman, @@ntessore]
    - ``hubble_distance`` - moved here (#31, #48) [@nstarman]

- ``HasHubbleTime`` (#48) [@nstarman, @@ntessore]
    - ``hubble_time`` - moved here (#31, #48) [@nstarman]

- ``HasHoverH0`` (#48) [@nstarman, @@ntessore]
    - ``H_over_H0``
        - Allow ``float`` input (#27) [@nstarman]
        - rename ``efunc`` to ``h_over_h0`` then ``H_over_H0`` (#31) [@nstarman]

- ``HubbleParameter`` (#31) [@nstarman]
    - Renamed ``HubbleParameter`` to ``HasHubbleParameter``, and back. (#33, #48) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasH0``, ``HasH``, ``HasHubbleDistance``, ``HasHubbleTime``, ``HasHoverH0`` (#48) [@nstarman, @@ntessore]

  Attributes:
    - ``h`` - removed
    - ``inv_efunc`` - removed
        - Allow ``float`` input (#27) [@nstarman]
        - removed (#31) [@nstarman]


- ``HasCriticalDensity0`` (#48) [@nstarman, @@ntessore]
    - ``critical_density0``
        - renamed from ``rho_critical0``

- ``HasCriticalDensity`` (#48) [@nstarman, @@ntessore]
    - ``critical_density``
        - renamed from ``rho_critical``
        - Allow ``float`` input (#27) [@nstarman]

- ``CriticalDensity`` (#38) [@nstarman]
    - Split from ``StandardCosmology``. (#38) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Renamed ``HasCriticalDensity`` to ``CriticalDensity``. (#48) [@nstarman, @@ntessore]
    - Subclass of ``HasCriticalDensity0`` and ``HasCriticalDensity`` (#48) [@nstarman, @@ntessore]


- ``HasTCMB0`` (#48) [@nstarman, @@ntessore]
    - ``T_cmb0`` - moved here (#25, #48) [@nstarman]
        - Renamed ``Tcmb0`` to ``T_cmb0`` (#47) [@nstarman]

- ``HasTCMB`` (#48) [@nstarman, @@ntessore]
    - ``T_cmb`` (#15) [@nstarman]
        - Allow ``float`` input (#27) [@nstarman]
        - Renamed ``Tcmb`` to ``T_cmb`` (#47) [@nstarman]

- ``TemperatureTCMB``  (#34) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``HasTCMB0`` and ``HasTCMB`` (#48) [@nstarman, @@ntessore]
    - Renamed ``HasTCMB`` to ``TemperatureTCMB``. (#48) [@nstarman, @@ntessore]


- ``HasScaleFactor0`` (#48) [@nstarman, @@ntessore]
    - ``scale_factor0`` - moved here (#25, #48) [@nstarman]

- ``HasScaleFactor`` (#48) [@nstarman, @@ntessore]
    - ``scale_factor``
        - Allow ``float`` input (#27) [@nstarman]

- ``ScaleFactor`` (#38) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Renamed ``HasScaleFactor`` to ``ScaleFactor``. (#48) [@nstarman, @@ntessore]
    - Subclass of ``HasScaleFactor0`` and ``HasScaleFactor`` (#48) [@nstarman, @@ntessore]


- ``HasComovingDistance`` (#51) [@nstarman]
    - ``comoving_distance``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasComovingTransverseDistance`` (#51) [@nstarman]
    - ``comoving_transverse_distance``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasComovingVolume`` (#51) [@nstarman]
    - ``comoving_volume``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasDifferentialComovingVolume`` (#51) [@nstarman]
    - ``differential_comoving_volume``
        - Allow ``float`` input (#27) [@nstarman]

- ``ComovingDistanceMeasures``
    - Subclass of ``HasComovingDistance``, ``HasComovingTransverseDistance``, ``HasComovingVolume``, ``HasDifferentialComovingVolume`` (#51) [@nstarman]


- ``HasAge`` (#51) [@nstarman]
    - ``age``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasLookbackTime`` (#51) [@nstarman, @@ntessore]
    - ``lookback_time``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasAngularDiameterDistance`` (#51) [@nstarman]
    - ``angular_diameter_distance``
        - Allow ``float`` input (#27) [@nstarman]

- ``HasLuminosityDistance`` (#51) [@nstarman]
    - ``luminosity_distance``
        - Allow ``float`` input (#27) [@nstarman]

- ``DistanceMeasures``
    - Split from ``FLRWCosmologyAPI``. (#18) [@nstarman]
    - Renamed ``BackgroundCosmologyAPI`` to ``FriedmannLemaitreRobertsonWalker`` (#30) [@nstarman]
    - Renamed ``FriedmannLemaitreRobertsonWalker`` to ``HasDistanceMeasures``. (#38) [@nstarman]
    - Generic wrt input type (#43) [@nstarman]
    - Subclass of ``TemperatureTCMB``, ``ScaleFactor`` (#48) [@nstarman, @@ntessore]
    - Subclass of ``HasAge``, ``HasLookbackTime``, ``ComovingDistanceMeasures``, ``HasAge``, ``HasLookbackTime``, ``HasAngularDiameterDistance``, ``HasLuminosityDistance``  (#51) [@nstarman]


- Documentation
    - format, layout, and rendering extensions (#40) [@@ntessore]

- ``HasInverseComovingDistance`` (#115) [@paddyroddy]
    - ``inv_comoving_distance`` (#115) [@paddyroddy]
