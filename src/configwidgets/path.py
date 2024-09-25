# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:40:48 2024

@author: kolja
"""
import logging
from enum import Enum
from pathlib import Path

from qtpy.QtCore import QSettings
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QFileDialog, QLineEdit, QRadioButton, QWidget
from qtpy.uic import loadUi

from .error import ConfigNotSetupError

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.INFO)


# TODO: add file/dir and filtyp to validation
# TODO: add multi filetyp selection


class FileTypeFilter(Enum):
    """ a class to define filter types."""
    empty = 0
    exe = 1
    txt = 2
    dat = 3
    nc = 4
    json = 5

    @property
    def filter_str(self):
        table = {
            0: [],
            1: ["executables (*.exe)"],
            2: ["text file (*.txt)"],
            3: ["data Files (*.dat)"],
            4: ["netCDF Files (*.nc)"],
            5: ["json Files (*.json)"]
            }
        return ";;".join(table[self.value])


class FileStatus(Enum):
    empty = "gray"
    valid = "green"
    invalid = "red"


class ConfigPathWidget(QWidget):
    """
    A combination of :py:class:`QComboBox`, a `QToolButton` and a `QLabel`.
    Select and display a path. Without setup this mimics a `QComboBox`.
    A `QSettings` instance can be setup to maintain state between program restarts.
    The button can be used to start a `QFileDialog` for easy selection.
    """
    def __init__(self, *args, **kwargs):
        """ initializing widget, mimics a QComboBox."""
        super().__init__(*args, **kwargs)
        loadUi(Path(__file__).parent / "static/pathselect.ui", self)
        self.logger = logging.getLogger(__name__)
        self.config = None
        self.name = None
        self.default = None
        self.mode = None
        self.filter = FileTypeFilter.empty
        self.isSetup = False
        self.label.hide()
        self.btn_select.hide()
        self.btn_select.clicked.connect(self.select)

    def setup(self, config: QSettings, name: str, default: Path = None, label: str = None,
              mode: str = None, filetyp=None):
        """
        Setup the connection to a `QSettings` instance to store state under the key.
        Optional: Set a default value. Optional: set a visual label.
        If mode is set to 'file' or 'directory' a selection button is enabled.
        If filetyp is set, a filter is used for the selection dialog.

        Parameters
        ----------
        config : QSettings
            The QSettings Instance.
        name : TYPE
            The key to store the data.
        default : Path, optional
            The default Path. The default is None.
        label : str, optional
            A visual label for the widget. The default is None.
        mode : str, optional
            Set to 'file' or 'directory' to use selection dialog. The default is None.
        filetyp : TYPE, optional
            A filter for the selection dialog. The default is None.

        """
        self.config = config
        self.name = name

        self.set_label(label)
        self.set_style(FileStatus.empty)
        self.set_mode(mode, filetyp)
        if self.isSetup:
            self.combo.textActivated.disconnect()
        else:
            self.combo.textActivated.connect(self.collect)
        self.load_value()

    def set_label(self, label: str = None):
        """ set the label of the widget."""
        if isinstance(label, str):
            self.label.setVisible(True)
            self.label.setText(label)
        else:
            self.label.setVisible(False)

    def set_style(self, style):
        """ set the style to valid/invalid/not set"""
        self.combo.lineEdit().setStyleSheet(f"color: {style.value};")

    def set_mode(self, mode: str = None, filetyp=None):
        """ set the selection mode to 'file'/'directory'.
        Optional: set a filter."""
        self.mode = mode
        self.btn_select.setVisible(self.mode is not None)
        self.set_filetyp(filetyp)

    def set_filetyp(self, filetyp: FileTypeFilter = FileTypeFilter.empty):
        """ Set a filter typ for the selection dialog. """
        if filetyp is None:
            filetyp = FileTypeFilter.empty
        if isinstance(filetyp, str) and filetyp in (f.name for f in FileTypeFilter):
            filetyp = FileTypeFilter[filetyp]
        if isinstance(filetyp, FileTypeFilter):
            self.filetyp = filetyp

    def set_icon(self, icon):
        """ set the icon of the selection button."""
        if isinstance(icon, str):
            icon = QIcon(icon)
        self.btn_select.setIcon(icon)

    def validate_text(self, text) -> Path | None:
        """ check if text is a valid path. If valid the value gets stored, else
        only the display shows the string. Changes the style accordingly."""
        if text == "<NOT SET>" or text == "" or text is None:
            return self.set_empty()
        path = Path(text).resolve()
        idx = self.combo.findText(text)

        if path.exists():
            self.set_style(FileStatus.valid)
            text = str(path)
            if idx < 0:     # is not in items
                self.combo.insertItem(1, text)
                self.combo.setCurrentIndex(1)
            else:           # remove and insert as resolved path
                self.combo.removeItem(idx)
                self.combo.insertItem(idx, text)
                self.combo.setCurrentIndex(idx)
            return path
        else:               # dont add to items
            self.combo.removeItem(idx)
            self.combo.setEditText(text)
            self.set_style(FileStatus.invalid)
            return None

    def load_value(self) -> Path | None:
        """ load text from config."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        val = self.config.value(self.name, type=str)
        if not Path(val).exists():
            val = self.default
        return self.validate_text(val)

    def set_empty(self):
        """ set value to None. """
        self.combo.setCurrentText("<NOT SET>")
        self.set_style(FileStatus.empty)
        self.config.setValue(self.name, None)
        return None

    def set_value(self, path) -> Path | None:
        """ set value to config and ui."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        path = self.validate_text(str(path))
        if path is not None:
            self.config.setValue(self.name, str(path.resolve()))
        return path

    def collect(self) -> Path | None:
        """ collect value from ui to config."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        text = self.combo.currentText()
        path = self.validate_text(text)
        if path is not None:
            self.config.setValue(self.name, str(path.resolve()))
        return path

    def select(self):
        # def select_path(self) -> Path:
        """ open a :py:class:`QFileDialog` to select a path."""
        if (self.config is None) | (self.name is None):
            raise ConfigNotSetupError(self)
        path = Path.home() if (path := self.load_value()) is None or not path.exists() else path
        options = dict(directory=str(path))
        if self.mode == "directory":
            options["caption"] = "select directory"
            path = QFileDialog.getExistingDirectory(self, **options)
        elif self.mode == "file":
            options["caption"] = f"select{' '+self.filetyp.name if self.filetyp else ''} file"
            options["filter"] = self.filetyp.filter_str
            path, f = QFileDialog.getOpenFileName(self, **options)
        else:
            self.logger.error("mode not set, selection not possible")
            return None

        if path != "":
            return self.set_value(Path(path))
        self.logger.info("selection canceld.")
