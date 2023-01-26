"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""


import pathlib
import sys
from importlib import import_module
from importlib.metadata import version as get_version

import tomli

# -- Project information -----------------------------------------------------


def get_authors() -> set[str]:
    """Get author information from ``pyproject.toml``s.

    Returns
    -------
    set[str]
        The authors.
    """
    authors: set[str] = set()
    cfg = pathlib.Path(__file__).parent.parent / "pyproject.toml"

    with cfg.open("rb") as f:
        toml = tomli.load(f)

    project = dict(toml["project"])
    authors.update({d["name"] for d in project["authors"]})

    return authors


project = "cosmology"
author = ", ".join(get_authors())
copyright = f"2002, {author}"  # noqa: A001

import_module(project)
package = sys.modules[project]

# The short X.Y version.
version = get_version("cosmology-api").split("-", 1)[0]
# The full version, including alpha/beta/rc tags.
release = get_version("cosmology-api")


# -- General configuration ---------------------------------------------------

# By default, highlight as Python 3.
highlight_language = "python3"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx_automodapi.automodapi",
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",
    "pytest_doctestplus.sphinx.doctestplus",
    "subprojecttoctree",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True

# Class documentation should contain *both* the class docstring and
# the __init__ docstring
autoclass_content = "both"

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
    "pythonloc": (
        "http://docs.python.org/",
        (
            None,
            (
                pathlib.Path(__file__).parent.parent
                / "local"
                / "python3_local_links.inv"
            ).resolve(),
        ),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://data.astropy.org/intersphinx/numpy.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference/",
        (None, "http://data.astropy.org/intersphinx/scipy.inv"),
    ),
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- automodapi extension -------------------------------------------------

automodapi_toctreedirnm = "api"


# -- matplotlib extension ----------------------------------------------------

plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False


# -- numpydoc extension -----------------------------------------------------

numpydoc_use_plots = True

# Don't show summaries of the members in each class along with the
# class' docstring
numpydoc_show_class_members = True

# Whether to create cross-references for the parameter types in the
# Parameters, Other Parameters, Returns and Yields sections of the docstring.
numpydoc_xref_param_type = True

# Words not to cross-reference. Most likely, these are common words used in
# parameter type descriptions that may be confused for classes of the same
# name. This can be overwritten or modified in packages and is provided here for
# convenience.
numpydoc_xref_ignore = {
    "or",
    "default",
    "optional",
    "positional-only",
    "keyword-only",
}

# -- subprojecttoctree extension --------------------------------------------

is_subproject = False
readthedocs_url = "https://cosmology.readthedocs.io/"
