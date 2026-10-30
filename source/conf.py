"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Path setup --------------------------------------------------------------

If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.
"""

# -- Project information -----------------------------------------------------

project = 'Rohde & Schwarz Instrument Control PyCharm Plugin'
# noinspection PyShadowingBuiltins
copyright = '© Rohde & Schwarz 2026'
author = 'Rohde & Schwarz'
master_doc = 'index'

# The full version, including alpha/beta/rc tags
release = '3.30.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'recommonmark'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.rest': 'restructuredtext',
}

autosectionlabel_prefix_document = True

add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['_static']
html_css_files = ['custom.css']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
autoclass_content = 'both'
pygments_style = 'zenburn'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
html_permalinks_icon = '#'

html_theme_options = {
    'navigation_depth': 3,
	'collapse_navigation': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
