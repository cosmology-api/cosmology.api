Changelog (``cosmology.api``)
=============================

0.1.0 (unreleased)
------------------

- CosmologyAPIConformant is the Protocol defining conformant cosmology classes.
  (#1) [nstarman]

-  CosmologyAPINamespace is the Protocol defining the main namespace of the
   API. (#1) [nstarman]

-  CosmologyConstantsAPINamespace is the Protocol defining the constants
   namespace of the API. (#1) [nstarman]

- CosmologyAPIConformantWrapper is the Protocol defining an API-conformant
  wrapper for a non-conformant cosmology class. (#4) [nstarman]

   - A default implementation is provided for ``__getattr__`` that passes
     through to the wrapped object. (#8) [nstarman]

- Added ``speed_of_light`` to the constants namespace. (#11) [nstarman]
