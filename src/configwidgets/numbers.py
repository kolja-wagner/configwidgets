# -*- coding: utf-8 -*-
"""
Definition of number subclasses.

@author: kolja
"""
from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox


class ConfigSpinBox(QSpinBox):

    def __init__(self, parent=None):
        super().__init__()
        self.name = None
        self.unit = None

    def setup(self, config: QSettings, name: str, default: int = 0, unit: str = ""):
        self.config = config
        self.set_name(name)
        self.set_unit(unit)
        self.set_default(default)

        self.setAlignment(Qt.AlignRight)
        self.load_value()
        self.editingFinished.connect(self.collect)

    def load_value(self) -> int:
        val = self.config.value(self.name, type=int, defaultValue=self.default)
        self.setValue(val)
        return val

    def set_value(self, val: int) -> int:
        self.setValue(val)
        self.config.setValue(self.name, val)
        return val

    def collect(self) -> int:
        val = self.value()
        self.config.setValue(self.name, val)
        return val

    def set_default(self, default: int):
        self.default = default

    def set_name(self, name: str):
        self.name = name

    def set_unit(self, unit: str):
        self.unit = unit
        self.setSuffix(f" {self.unit}")


class ConfigDoubleSpinBox(QDoubleSpinBox):

    def __init__(self, parent=None):
        super().__init__()
        self.name = None
        self.unit = None

    def setup(self, config: QSettings, name: str, default: float = 0, unit: str = ""):
        self.config = config
        self.set_name(name)
        self.set_unit(unit)
        self.set_default(default)

        self.setAlignment(Qt.AlignRight)
        self.load_value()
        self.editingFinished.connect(self.collect)

    def load_value(self) -> float:
        val = self.config.value(self.name, type=float, defaultValue=self.default)
        self.setValue(val)
        return val

    def set_value(self, val: float) -> float:
        self.setValue(val)
        self.config.setValue(self.name, val)
        return val

    def collect(self) -> float:
        val = self.value()
        self.config.setValue(self.name, val)
        return val

    def set_default(self, default: float):
        self.default = default

    def set_name(self, name: str):
        self.name = name

    def set_unit(self, unit: str):
        self.unit = unit
        self.setSuffix(f" {self.unit}")
