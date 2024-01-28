# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:56:14 2024

@author: kolja
"""

import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import QSettings
from PyQt5.uic import loadUi


from configwidgets import ConfigCheckBox

class ExampleWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        loadUi(__file__+"/../example.ui", self)
        
        self.config = QSettings("k.wagner", "configsettings-example")
        self.setup_widget()
    def setup_widget(self):
        self.checkBox.setup(self.config, "checkBox")
    
    def setup_actions(self):
        self.btn_show.clicked.connect(self.show_settings)
        self.btn_reset.clicked.connect(self.reset_settings)
        
    def show_settings(self):
        print(f"show all in {self.config.fileName()}")
        keys = self.config.allKeys()
        settings = {k: self.config.value(k) for k in keys}
        pprint(settings)
        
    def reset_settings(self):
        print(f"reset {self.config.fileName()}")
        self.config.clear()


def start_example():
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.setup_actions()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    start_example()    