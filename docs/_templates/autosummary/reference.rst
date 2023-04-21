{{ name | escape | underline }}

{% if protocols -%}
.. rubric:: Protocols

.. currentmodule:: cosmology.api
{% for protocol in protocols %}
{% if loop.first %}.. {{ objtype }}:: {{ protocol }}
{%- else %}{% for c in objtype %} {% endfor %}      {{ protocol }}
{%- endif %}
{%- endfor %}
   :nocontentsentry:

{% endif -%}

.. rubric:: Reference

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}
