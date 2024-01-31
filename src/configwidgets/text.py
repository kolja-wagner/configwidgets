# -*- coding: utf-8 -*-
"""
Definition of text based Widgets.

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QLineEdit


class ConfigLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.name = None
        self.default = None

    def setup(self, config: QSettings, name: str, default: str = ""):
        self.config = config
        self.set_name(name)
        self.set_default(default)

        self.load_value()
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