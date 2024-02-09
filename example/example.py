# -*- coding: utf-8 -*-
"""
Create a simple widget to show the functionality of the configswidget package.

@author: kolja
"""
import logging
import sys
from pprint import pformat

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget
from PyQt5.uic import loadUi

from configwidgets import ConfigCheckBox


class ExampleWindow(QWidget):
    EXIT_CODE_REBOOT = -42

    def __init__(self):
        super().__init__()
        loadUi(__file__ + "/../example.ui", self)
        self.config = QSettings("k.wagner", "configwidgets-example")
        self.setup_widget()

    def setup_widget(self):
        self.checkBox.setup(self.config, "checkBox")
        self.radioButton_1.setup(self.config, "radioButton1")
        self.radioButton_2.setup(self.config, "radioButton2")

        self.spinBox.setup(self.config, "spinBox")
        self.doubleSpinBox.setup(self.config, "doubleSpinBox")
        
        self.lineEdit.setup(self.config, "lineEdit")
        self.comboBox.setup(self.config, "comboBox", ["abc","def", "ghi"], default="def")

        self.dateEdit.setup(self.config, "dateEdit")
        self.timeEdit.setup(self.config, "timeEdit")
        self.dateTimeEdit.setup(self.config, "dateTimeEdit")

        self.widget_path.setup(self.config, "pathWidget_path", label="directory", mode="directory")
        self.widget_file.setup(self.config, "pathWidget_file", label="txt file", 
                               mode="file", filetyp="txt")
        

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
