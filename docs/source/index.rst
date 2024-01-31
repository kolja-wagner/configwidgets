.. configwidgets documentation master file, created by
   sphinx-quickstart on Mon Jan 29 14:33:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

configwidgets - sync widget state to QSettings.
===============================================

while developing a pyqt5 based gui application for running uvspec simulations,
implementing the same functions to load and collect checkbox and spinbox states
demonstrated the necessity of a dedicated package for persistent wiget states.

The approach of the `pyqtconfig <https://pypi.org/project/pyqtconfig/>`_ package
didnt match the project structure, therefore a new package was created.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   setup
   package

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
