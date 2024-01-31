package
=======

the contents of the :mod:`configwidgets` package.


concept
-------

All widgets are build with the same concept:

* subclass a QtWidget. The default behaviour is the same.
* define a `setup` method. 

  * This assigns a :py:class:`QSettings` instance,
  
  * and a key, where the data is stored. 
  
  * a default value is used when the key doesnt exists.

* the :func:`load_value` method load the value from the QSettings instance into the widget state. :func:`setup` calls this method.

* the :func:`collect` method saves the current widget state into the QSettings instance. The method is connected to the "state changed" signal (i.e. :attr:`editingFinished`, :attr:`toggled`)

* the :func:`set_value` method sets the parameter to state and QSettings.

The "only" change is the type of the value and the state-change signal.

show case
---------

The following :class:`ConfigCheckBox` provides an example, the other classes are defined alike:

.. autoclass:: configwidgets.ConfigCheckBox
   :members:
   :special-members: __init__
   :member-order: bysource
   
content
-------

.. toctree::
   :maxdepth: 2

   package_buttons
   package_text
   package_numbers
   package_datetime

