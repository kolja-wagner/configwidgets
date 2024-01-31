# -*- coding: utf-8 -*-
"""
Definition of container widgets.

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QGroupBox

class ConfigGroupBox(QGroupBox):
    """
    A subclass of :py:class:`QGroupBox`. Can be setup with a link to `QSettings` instance
    to maintain state between program restarts. Supports toggeling the visibility.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a checkable ConfigCheckBox.

        Parameters
        ----------
        text : str, optional
            The title of the groupbox.
        parent : QWidget, optional
            The parent widget of the groupbox. The default is None.
        """
        super().__init__(*args, **kwargs)
        self.setCheckable(True)
        self.config = None
        self.name = None
        self.default = False
        self.toggle_vis = False

    def setup(self, config: QSettings, name: str, default: bool = False, toggle_visibility: bool = False):
        """
        Setup the link to a :py:class:`QSettings` instance for this groupbox.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        default : bool, optional
            The default value. The default is False.
        toggle_visibility: bool, optional
            If true, than the check state also controls the visibility of the content.
        """
        self.config = config
        self.set_name(name)
        self.set_default(default)
        self.set_toggle_visibility(toggle_visibility)

        self.load_value()
        self.toggled.connect(self.collect)

    def set_name(self, name: str):
        """
        set the QSetting-Key for this groupbox.
        """
        self.name = name

    def set_default(self, default: bool):
        """ set the default value for retrieving the value. """
        self.default = default
        
    def set_toggle_visibility(self, toggle: bool):
        self.toggle_vis = toggle

    def load_value(self) -> bool:
        """ load the state from the QSettings instance to the widget state.
        If the key is not defined, the :attr:`default` is used instead.
        """
        if self.config is None:
            return
        val = self.config.value(self.name, type=bool, defaultValue=self.default)
        self.setChecked(val)
        self.activate(val)
        return val

    def set_value(self, val: bool) -> bool:
        """ set a value to the widget state and the QSettings Instance."""
        if self.config is None:
            return
        self.setChecked(val)
        self.collect()
        return val

    def collect(self) -> bool:
        """ collect the widget state and store in QSettings Instance.
        Gets connected to the :func:`toggled` signal."""
        if self.config is None:
            return
        val = self.isChecked()
        if self.name is not None:
            self.config.setValue(self.name, val)
        self.activate(val)
        return val
    
    def activate(self, val: bool):
        """ if setup, change the visibility of the content of this widget."""
        if not self.toggle_vis:
            return
        for c in self.children():
            if not c.isWidgetType():
                continue
            c.setVisible(val)
        