
Components
==========

.. currentmodule:: cosmology.api

This page contains a list of protocols for components of a cosmology.  These
are not only components in the physical sense (e.g. "matter", "baryons") but
more generally groups of closely related methods and properties (e.g. "Hubble
parameter, time, and distance").

At a higher level of abstraction, the sum of components makes a :doc:`cosmology
</api/cosmology>`.

At a lower level of abstraction, a component consists of individual
:doc:`attributes </api/protocols>`.

Physical Components
-------------------

.. autoclass:: NeutrinoComponent()
.. autoclass:: BaryonComponent()
.. autoclass:: PhotonComponent()
.. autoclass:: DarkMatterComponent()
.. autoclass:: MatterComponent()
.. autoclass:: DarkEnergyComponent()
.. autoclass:: CurvatureComponent()
.. autoclass:: TotalComponent()

.. autoclass:: CriticalDensity()


Distance Measures
-----------------

.. autoclass:: HubbleParameter()
.. autoclass:: ScaleFactor()
.. autoclass:: TemperatureCMB()
.. autoclass:: LookbackDistanceMeasures()
.. autoclass:: ComovingDistanceMeasures()
.. autoclass:: ProperDistanceMeasures()

.. autoclass:: DistanceMeasures()
