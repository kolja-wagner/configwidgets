# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'configwidgets'
copyright = '2024, Kolja Wagner'
author = 'Kolja Wagner'

import configwidgets
release = configwidgets.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',

    'sphinx_qt_documentation',
    'sphinx_copybutton',
    ]
templates_path = ['_templates']
exclude_patterns = []


# -- options for intersphinx
qt_documentation = "PySide6"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    }
intersphinx_disabled_reftypes = ["*"]


# -- options for copybutton
copybutton_prompt_text = r"/>>>|\.\.\.|\([a-zA-Z]+\)\ \$\ |\$\ /gm"
copybutton_prompt_is_regexp = True


# -- options for myst-nb
nb_number_source_lines = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {"navigation_with_keys": True}
