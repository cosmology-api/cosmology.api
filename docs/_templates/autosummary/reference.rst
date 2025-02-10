{{ name | escape | underline }}

{% if class -%}
Protocol: :class:`~cosmology.api.{{ class }}`
{% endif %}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}
