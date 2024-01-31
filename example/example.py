# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:56:14 2024

@author: kolja
"""

import sys
from pprint import pprint

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget
from PyQt5.uic import loadUi

from configwidgets import ConfigCheckBox


class ExampleWindow(QWidget):
    EXIT_CODE_REBOOT = -42
    
    def __init__(self):
        super().__init__()
        loadUi(__file__+"/../example.ui", self)
        self.config = QSettings("k.wagner", "configsettings-example")
        self.setup_widget()
        
    def setup_widget(self):
        self.checkBox.setup(self.config, "checkBox")
        self.spinBox.setup(self.config, "spinBox")
        self.doubleSpinBox.setup(self.config, "doubleSpinBox")
        self.lineEdit.setup(self.config, "lineEdit")
        
        self.dateEdit.setup(self.config, "dateEdit")
        self.timeEdit.setup(self.config, "timeEdit")
        self.dateTimeEdit.setup(self.config, "dateTimeEdit")
    
    def setup_actions(self):
        self.btn_show.clicked.connect(self.show_settings)
        self.btn_reset.clicked.connect(self.reset_settings)
        self.btn_restart.clicked.connect(self.restart)
        
    def show_settings(self):
        print(f"show all in {self.config.fileName()}")
        keys = self.config.allKeys()
        settings = {k: self.config.value(k) for k in keys}
        pprint(settings)
        
    def reset_settings(self):
        print(f"reset {self.config.fileName()}")
        self.config.clear()
        
    def restart(self):
        QApplication.instance().exit(self.EXIT_CODE_REBOOT)


def start_example():
    current_exit_code = ExampleWindow.EXIT_CODE_REBOOT
    while current_exit_code == ExampleWindow.EXIT_CODE_REBOOT:
        app = QApplication(sys.argv)
        window = ExampleWindow()
        window.setup_actions()
        window.show()
        current_exit_code = app.exec()
        app = None



if __name__ == "__main__":
    start_example()    