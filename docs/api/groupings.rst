
Groupings
=========

.. toctree::
   :hidden:

   cosmology
   components
   namespaces

These protocols allow you to specify and inspect which attributes are
supported by a given cosmology object.
If you do not require static or dynamic type checking of cosmology instances,
the :doc:`reference </api/reference>` provides a flat list of all methods and
attributes which can potentially be supported by cosmology instances.


Protocol hierarchy
------------------

The cosmology protocols are arranged grouped in levels:

* High-level :doc:`cosmology protocols </api/cosmology>` which
  describe fully-featured cosmology objects.
* Intermediate-level :doc:`component protocols </api/components>` which
  describe individual functional groups such as e.g. the physical matter and
  baryon components, or the Hubble parameters :math:`H_0` and :math:`H(z)`.
* Low-level :doc:`attribute protocols </api/protocols>` which describe the
  existence of individual methods and properties.
* Meta-level :doc:`namespace protocols </api/namespaces>` which describe the
  cosmology API itself.
