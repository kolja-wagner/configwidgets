# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:07:43 2024

@author: kolja
"""

from datetime import date as pydate
from datetime import datetime
from datetime import time as pytime

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDateEdit, QDateTimeEdit, QTimeEdit


class ConfigDateTimeEdit(QDateTimeEdit):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.name = None
    
    def setup(self, config: QSettings, name: str, default: datetime =  None):
        self.config = config
        self.set_name(name)
        self.set_default(default)
        
        self.load_value()
        self.editingFinished.connect(self.collect)
        
    def set_name(self, name: str):
        self.name = name
        
    def set_default(self, default: datetime=None):
        if default is None:
            default = datetime.utcnow()
        self.default = default
        
    def collect(self) -> datetime:
        dt = self.dateTime().toPyDateTime()
        if self.name is not None:
            self.config.setValue(self.name, dt)
        return dt
            
    def load_value(self) -> datetime:
        dt = self.config.value(self.name, defaultValue=self.default, type=datetime)
        self.setDateTime(dt)
        return dt
    
    def set_value(self, dt: datetime) -> datetime:
        self.setDateTime(dt)
        self.collect()
        return dt
    
    
class ConfigDateEdit(QDateEdit):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.name = None
    
    def setup(self, config: QSettings, name: str, default: pydate = None):
        self.config = config
        self.set_name(name)
        self.set_default(default)
        
        self.load_value()
        self.editingFinished.connect(self.collect)
        
    def set_name(self, name: str):
        self.name = name
        
    def set_default(self, default: pydate=None):
        if default is None:
            default = pydate.today()
        self.default = default
        
    def collect(self) -> pydate:
        d = self.date().toPyDate()
        if self.name is not None:
            self.config.setValue(self.name, d)
        return d
            
    def load_value(self) -> pydate:
        d = self.config.value(self.name, defaultValue=self.default, type=pydate)
        self.setDate(d)
        return d
    
    def set_value(self, date: pydate) -> pydate:
        self.setDate(date)
        self.collect()
        return date


class ConfigTimeEdit(QTimeEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.name = None
    
    def setup(self, config: QSettings, name: str, default: pytime=None):
        self.config = config
        self.set_name(name)
        self.set_default(default)
        
        self.load_value()
        self.editingFinished.connect(self.collect)
        
    def set_name(self, name: str):
        self.name = name
        
    def set_default(self, default: pytime=None):
        if default is None:
            default = datetime.utcnow().time()
        self.default = default
        
    def collect(self) -> pytime:
        t = self.time().toPyTime()
        if self.name is not None:
            self.config.setValue(self.name, t)
        return t
            
    def load_value(self) -> pytime:
        t = self.config.value(self.name, defaultValue=self.default, type=pydate)
        self.setTime(t)
        return t
    
    def set_value(self, time: pytime):
        self.setTime(time)
        self.collect()
        return time
