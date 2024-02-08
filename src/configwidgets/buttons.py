# -*- coding: utf-8 -*-
"""
Definition of action based widgets.

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QCheckBox, QRadioButton

from .error import ConfigNotSetupError

class ConfigCheckBox(QCheckBox):
    """
    A subclass of :py:class:`QCheckBox`. Can be setup with a link to `QSettings` instance
    to maintain state between program restarts.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a ConfigCheckBox.
        Other than declaring default values as `None` the super constructor is called.

        Parameters
        ----------
        text : str
            The text of the checkbox.
        parent : QWidget, optional
            The parent widget of the checkbox. The default is None.
        """
        super().__init__(*args, **kwargs)
        self.config = None
        self.name = None
        self.default = False

    def setup(self, config: QSettings, name: str, default: bool = False):
        """
        Setup the link to a :py:class:`QSettings` instance for this checkbox.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        default : bool, optional
            The default value. The default is False.
        """
        self.config = config
        self.set_name(name)
        self.set_default(default)

        self.load_value()
        self.toggled.connect(self.collect)

    def set_name(self, name: str):
        """
        set the QSetting-Key for this checkbox.
        """
        self.name = name

    def set_default(self, default: bool):
        """ set the default value for retrieving the value. """
        self.default = default

    def load_value(self) -> bool:
        """ load the state from the QSettings instance to the widget state.
        If the key is not defined, the :attr:`default` is used instead.
        
        Raises
        ------
        ConfigNotSetupError
            Raises an Error if the setup function wasnt called.
        """
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        val = self.config.value(self.name, type=bool, defaultValue=self.default)
        self.setChecked(val)
        return val

    def set_value(self, val: bool) -> bool:
        """ set a value to the widget state and the QSettings Instance.
        
        Raises
        ------
        ConfigNotSetupError
            Raises an Error if the setup function wasnt called.
        """
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        self.setChecked(val)
        self.collect()
        return val

    def collect(self) -> bool:
        """
        collect the widget state and store in QSettings Instance.
        Gets connected to the :func:`toggled` signal.
        
        Raises
        ------
        ConfigNotSetupError
            Raises an Error if the setup function wasnt called.
        """
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        val = self.isChecked()
        self.config.setValue(self.name, val)
        return val


class ConfigRadioButton(QRadioButton):
    """
    A subclass of :py:class:`QRadioButton`. Can be setup with a link
    to `QSettings` instance to maintain state between program restarts.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a ConfigRadioButton.
        Other than declaring default values as `None` the super constructor is called.

        Parameters
        ----------
        text : str
            The text of the radiobutton.
        parent : QWidget, optional
            The parent widget of the radiobutton. The default is None.
        """
        super().__init__(*args, **kwargs)
        self.config = None
        self.name = None
        self.default = False

    def setup(self, config: QSettings, name: str, default: bool = False):
        """
        Setup the link to a :py:class:`QSettings` instance for this radiobutton.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        default : bool, optional
            The default value. The default is False.
        """
        self.config = config
        self.set_name(name)
        self.set_default(default)

        self.load_value()
        self.toggled.connect(self.collect)

    def set_name(self, name: str):
        """
        set the QSetting-Key for this radiobutton.
        """
        self.name = name

    def set_default(self, default: bool):
        """ set the default value for retrieving the value. """
        self.default = default

    def load_value(self) -> bool:
        """ load the state from the QSettings instance to the widget state.
        If the key is not defined, the :attr:`default` is used instead.
        """
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        val = self.config.value(self.name, type=bool, defaultValue=self.default)
        self.setChecked(val)
        return val

    def set_value(self, val: bool) -> bool:
        """ set a value to the widget state and the QSettings Instance."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        self.setChecked(val)
        self.collect()
        return val

    def collect(self) -> bool:
        """ collect the widget state and store in QSettings Instance.
        Gets connected to the :func:`toggled` signal."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        val = self.isChecked()
        self.config.setValue(self.name, val)
        return val
