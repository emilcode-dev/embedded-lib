# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Embedded Lib'
copyright = '2025, Ephraim Eckl'
author = 'Ephraim Eckl'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "breathe",
]

breathe_projects = {
    "EmbeddedLib": "../builddoxy/xml"
}
breathe_default_project = "EmbeddedLib"

templates_path = ['_templates']
exclude_patterns = []

language = 'C'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
