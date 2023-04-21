
Protocols
=========

.. toctree::
   :hidden:

   cosmology
   components
   attributes
   namespaces

[Introduction about protocols in the cosmology API.]

The :doc:`reference </api/reference>` provides a flat list of all attributes
which can potentially be supported by cosmology instances.  Conversely, the
protocols allow you to specify and inspect which attributes are supported by a
given cosmology object.


Protocol hierarchy
------------------

The cosmology protocols are arranged grouped in levels:

* High-level :doc:`cosmology protocols </api/cosmology>` which
  describe fully-featured cosmology objects.
* Intermediate-level :doc:`component protocols </api/components>` which
  describe individual functional groups such as e.g. the physical matter and
  baryon components, or the Hubble parameters :math:`H_0` and :math:`H(z)`.
* Low-level :doc:`attribute protocols </api/attributes>` which describe the
  existence of individual methods and properties.
* Meta-level :doc:`namespace protocols </api/namespaces>` which describe the
  cosmology API itself.

[Some additional explanation about the hierarchy.]


Using protocols
---------------

[Introduction and examples of how these protocols are to be used.]
