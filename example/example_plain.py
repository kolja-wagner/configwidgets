# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:39:49 2024

@author: kolja
"""
import sys
from pprint import  pformat

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget
from PyQt5.uic import loadUi

import logging

class ExampleWindow(QWidget):
    EXIT_CODE_REBOOT = -42

    def __init__(self):
        super().__init__()
        loadUi(__file__ + "/../example_plain.ui", self)
        self.config = QSettings("k.wagner", "configwidgets-example")
        self.setup_widget()

    def setup_widget(self):
        self.plainTextEdit.setup(self.config, "plainText", default="", autocollect=False)
        self.btn_collect.clicked.connect(self.plainTextEdit.collect)

        
    def setup_actions(self):
        self.btn_show.clicked.connect(self.show_settings)
        self.btn_reset.clicked.connect(self.reset_settings)
        self.btn_restart.clicked.connect(self.restart)

    def show_settings(self):
        logging.info(f"show all in {self.config.fileName()}")
        keys = self.config.allKeys()
        settings = {k: self.config.value(k) for k in keys}
        logging.info(pformat(settings))

    def reset_settings(self):
        logging.info(f"reset {self.config.fileName()}")
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
