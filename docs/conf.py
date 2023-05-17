# ruff: noqa

"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""


import os
import sys
import tomli

sys.path.append(os.path.abspath("../src"))


# -- Project information -----------------------------------------------------


def read_pyproject():
    """Get author information from package metadata."""
    with open(os.path.abspath("../pyproject.toml"), "rb") as f:
        toml = tomli.load(f)

    project = dict(toml["project"])
    version = project["version"]
    authors = ", ".join(d["name"] for d in project["authors"])

    return version, authors


package_version, package_authors = read_pyproject()

project = "cosmology.api"
author = package_authors
copyright = f"2023, {author}"


# The full version, including alpha/beta/rc tags.
release = package_version
# The short X.Y version.
version = release.partition("-")[0]


# -- General configuration ---------------------------------------------------

sys.path.append(os.path.abspath("./_ext"))

# By default, highlight as Python 3.
highlight_language = "python3"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_ext_autosummary_context",
    "sphinx_ext_cosmology_api",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog = """
.. |author| replace:: {author}

.. _Python: http://www.python.org
"""

intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://data.astropy.org/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://data.astropy.org/intersphinx/numpy.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference/",
        (None, "https://docs.scipy.org/doc/scipy/objects.inv"),
    ),
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f"{project} v{release}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- autodoc extension -------------------------------------------------------

# The default options for autodoc directives. They are applied to all autodoc
# directives automatically. It must be a dictionary which maps option names to
# the values.
autodoc_default_options = {
    "members": False,
    "inherited-members": False,
    "show-inheritance": True,
}


add_module_names = False

# autodoc_class_signature = "separated"

autosummary_generate = True


# -- numpydoc extension ------------------------------------------------------

# Whether to show all members of a class in the Methods and Attributes sections
# automatically. True by default.
numpydoc_show_class_members = True

# Whether to show all inherited members of a class in the Methods and
# Attributes sections automatically. If it's false, inherited members won't
# shown. True by default.
numpydoc_show_inherited_class_members = True

# Whether to create a Sphinx table of contents for the lists of class methods
# and attributes. If a table of contents is made, Sphinx expects each entry to
# have a separate page. True by default.
numpydoc_class_members_toctree = False

# A regular expression matching citations which should be mangled to avoid
# conflicts due to duplication across the documentation. Defaults to '[\w-]+'.
# > numpydoc_citation_re = '[\w-]+'

# Whether to format the Attributes section of a class page in the same way as
# the Parameter section. If it's False, the Attributes section will be
# formatted as the Methods section using an autosummary table. True by default.
numpydoc_attributes_as_param_list = False

# Whether to create cross-references for the parameter types in the
# Parameters, Other Parameters, Returns and Yields sections of the docstring.
numpydoc_xref_param_type = True

# Words not to cross-reference. Most likely, these are common words used in
# parameter type descriptions that may be confused for classes of the same
# name. This can be overwritten or modified in packages and is provided here
# for convenience.
numpydoc_xref_ignore = {
    "or",
    "default",
    "optional",
    "positional-only",
    "keyword-only",
}

# -- copybutton extension ------------------------------------------------------

copybutton_exclude = ".linenos, .gp, .go"
