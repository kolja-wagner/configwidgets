
changelog
=========

v1.4.*
------
* Adding full tests for all widgets.
* Adding ConfigNotSetupError. This error is raised allways, when load_value/set_value/collect is called with out setup.
* Full rewrite for ConfigPathWidget. Now based on QComboBox and with a history of the current session, also colored validation.
* Change dependency from :code:`PyQt5` to :code:`qtpy`. Update :code:`pyproject.toml` with dependencies.


v1.3.*
------
Implement the first custom widgets

* ConfigPathWidget

v1.2.*
------
Improving the documentation, implementation of the following widgets:

* ConfigGroupBox
* ConfigComboBox
* ConfigPlainTextEdit


v1.1.*
------
fixing major bugs

v1.0.*
------
setup the basic package, including docs and example.
implementation of the following widgets:

* ConfigCheckBox, ConfigRadioButton
* ConfigSpinBox, ConfigDoubleSpinBox
* ConfigLineEdit
* ConfigDateEdit, ConfigTimeEdit, ConfigDateTimeEdit

