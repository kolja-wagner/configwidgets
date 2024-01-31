# configwidgets

Subclassing `QWidgets` to save the widget state in a `QSettings` Instance.
A `setup` method links the widget to key within the `QSettings` instance. 
The value is loaded during setup and gets stored when the widget state changes.
Without calling this method, the widget has no special behaviour.

See the following snippet for a minimal example:
```
from PyQt5.QtCore import QSettings
from configwidgets import ConfigCheckBox

config = QSettings()
checkBox = ConfigCheckBox()
checkBox.setup(config, "checkBox")
```

## setup

install the package via pip:
```
pip install configwidgets
```

The full documentation can be found under 
[configwidgets documentation](https://configwidgets.readthedocs.io/en/latest/index.html)
The source code can be found under
[configwidgets repository](https://github.com/kolja-wagner/configwidgets)