# -*- coding: utf-8 -*-
"""
Definition of text based Widgets.

@author: kolja
"""
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QLineEdit, QComboBox


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


class ConfigComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__()
        self.name = None
        self.default = None

    def setup(self, config: QSettings, name: str, options: list[str], 
              default: str = None, enable_custom: bool=False):
        self.config = config
        self.set_name(name)
        self.set_options(options)
        self.set_default(default)
        self.load_value() 
        self.textActivated.connect(self.collect)
        # # TODO: enable new items
        # self.setEditable(True)
        
    def set_name(self, name):
        self.name = name
        
    def set_options(self, options: list[str]):
        self.options = options
        
        for key in self.options:
            self.addItem(str(key))
        # TODO: add to QSettings

    def set_default(self, default: str):
        if default is None:
            default = self.options[0]
        self.default = default

    def collect(self) -> str:
        """ save text in config."""
        print("collect")
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

        
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    keys = ["abc", "def", "ghi"]
    
    config = QSettings("k.wagner", "configsettings-example")

    app = QApplication(sys.argv)
    window = ConfigComboBox() 
    window.setup(config, "comboBox", keys, default=keys[1])

    window.show()
    sys.exit(app.exec())

