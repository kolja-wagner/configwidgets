# -*- coding: utf-8 -*-
"""
Definition of text based Widgets.

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit


class ConfigLineEdit(QLineEdit):
    """
    A subclass of :py:class:`QLineEdit`. Can be setup with a link to `QSettings` instance
    to maintain state between program restarts.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.default = None

    def setup(self, config: QSettings, name: str, default: str = "", autocollect: bool=True):
        """
        Setup the link to a :py:class:`QSettings` instance for this lineedit.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        default : bool, optional
            The default value. The default is False.
        autocollect : bool, optional
            If true, every change is collected.
        """
        self.config = config
        self.set_name(name)
        self.set_default(default)

        self.load_value()
        if autocollect:
            self.editingFinished.connect(self.collect)

    def collect(self) -> str:
        """ save text in config."""
        val = self.text()
        self.config.setValue(self.name, val)
        return val

    def load_value(self) -> str:
        """ load text from config."""
        val = self.config.value(self.name, type=str, defaultValue=self.default)
        self.setText(val)
        return val

    def set_value(self, val: str) -> str:
        """ to widget and config."""
        self.setText(val)
        self.collect()
        return val

    def set_name(self, name: str):
        self.name = name

    def set_default(self, default: str):
        self.default = default


class ConfigComboBox(QComboBox):
    """
    A subclass of :py:class:`QComboBox`. Can be setup with a link to `QSettings` instance
    to maintain state between program restarts.
    """
    def __init__(self, parent=None):
        """
        Initialize a ConfigRadioButton. Other than declaring default values as `None` the super constructor is called.

        Parameters
        ----------
        parent : QWidget, optional
            The parent widget of the radiobutton. The default is None.
        """
        super().__init__(parent=parent)
        self.name = None
        self.default = None

    def setup(self, config: QSettings, name: str, items: list[str], 
              default: str = None, enable_custom: bool=False):
        """
        Setup the link to a :py:class:`QSettings` instance for this combobox.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        items: list[str]
            The list of items to be displayed.
        default : bool, optional
            The default value. The default is False.
        """
        self.config = config
        self.set_name(name)
        self.set_items(items)
        self.set_default(default)
        self.load_value() 
        self.textActivated.connect(self.collect)
        # # TODO: enable new items
        # self.setEditable(True)
        
    def set_name(self, name):
        self.name = name
        
    def set_items(self, items: list[str]):
        """ set the items of the combobox."""
        self.items = items
        self.clear()
        for key in self.items:
            self.addItem(str(key))
        # TODO: add to QSettings

    def set_default(self, default: str):
        if default is None:
            default = self.items[0]
        self.default = default

    def collect(self) -> str:
        """ save text in config."""
        val = self.currentText()
        self.config.setValue(self.name, val)
        # TODO: save new values to QSettings
        return val

    def load_value(self) -> str:
        """ load text from config."""
        val = self.config.value(self.name, type=str, defaultValue=self.default)
        self.setCurrentText(val)
        return val

    def set_value(self, val: str) -> str:
        """ to widget and config."""
        self.setText(val)
        self.collect()
        return val

class ConfigPlainTextEdit(QPlainTextEdit):
    """
    A subclass of :py:class:`QPlainTextEdit`. Can be setup with a link to `QSettings` instance
    to maintain state between program restarts.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.default = None

    def setup(self, config: QSettings, name: str, default: str = "", autocollect: bool=False):
        """
        Setup the link to a :py:class:`QSettings` instance for this plaintextedit.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The QSettings key to store the synced value.
        default : bool, optional
            The default value. The default is False.
        autocollect: bool, optional
            When False the state is not automatically saved. The default is False.
        """
        self.config = config
        self.set_name(name)
        self.set_default(default)

        self.load_value()
        if autocollect:
            self.textChanged.connect(self.collect)

    def collect(self) -> str:
        """ save text in config."""
        val = self.toPlainText()
        self.config.setValue(self.name, val)
        return val

    def load_value(self) -> str:
        """ load text from config."""
        val = self.config.value(self.name, type=str, defaultValue=self.default)
        self.setPlainText(val)
        return val

    def set_value(self, val: str) -> str:
        """ to widget and config."""
        self.setPlainText(val)
        self.collect()
        return val

    def set_name(self, name: str):
        self.name = name

    def set_default(self, default: str):
        self.default = default


