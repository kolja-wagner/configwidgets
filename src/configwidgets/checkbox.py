# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:53:58 2024

@author: kolja
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:52:15 2024

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QCheckBox

class ConfigCheckBox(QCheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.default = False
        
    def setup(self, config: QSettings, name: str, default: bool=False):
        self.config = config
        self.set_name(name)
        self.set_default(default)
        
        self.load_value()
        self.toggled.connect(self.collect)
        
    def set_name(self, name: str):
        self.name = name
        
    def set_default(self, default: bool):
        self.default=default
        
    def load_value(self):
        val = self.config.value(self.name, type=bool, defaultValue=self.default)
        self.setChecked(val)
        return val
    
    def set_value(self, val: bool):
        self.setChecked(val)
        self.collect()
        return val
        
    def collect(self):
        val = self.isChecked()
        if self.name is not None:
            self.config.setValue(self.name, val)
            