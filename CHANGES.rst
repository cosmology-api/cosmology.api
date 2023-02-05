Changelog (``cosmology.api``)
=============================

0.1.0 (unreleased)
------------------

- CosmologyAPI is the Protocol defining conformant cosmology classes.
  (#1) [nstarman]

-  CosmologyAPINamespace is the Protocol defining the main namespace of the
   API. (#1) [nstarman]

-  CosmologyConstantsAPINamespace is the Protocol defining the constants
   namespace of the API. (#1) [nstarman]

- CosmologyWrapperAPI is the Protocol defining an API-conformant
  wrapper for a non-conformant cosmology class. (#4) [nstarman]

   - A default implementation is provided for ``__getattr__`` that passes
     through to the wrapped object. (#8) [nstarman]

- Added ``speed_of_light`` to the constants namespace. (#11) [nstarman]

- Break the standard cosmology into a composition of components: (#25) [nstarman]
   - DarkEnergyComponent
   - GlobalCurvatureComponent
   - PhotonComponent
   - NeutrinoComponent
   - MatterComponent
      - DarkMatterComponent
      - BaryonComponent
