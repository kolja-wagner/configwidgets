# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:40:48 2024

@author: kolja
"""
import logging
from pathlib import Path
from enum import Enum

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QRadioButton, QWidget
from PyQt5.uic import loadUi

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.INFO)


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


class ConfigPathWidget(QWidget):
    """
    A combination of :py:class:`ConfigLineEdit`, a `QToolButton` and a `QLabel`.
    Select and display a path. Without setup this mimics a `QLineEdit`.
    A `QSettings` instance can be setup to maintain state between program restarts.
    The button can be used to start a `QFileDialog` for easy selection.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi(Path(__file__).parent / "static/pathselect.ui", self)
        self.logger = logging.getLogger(__name__)
        self.config = None
        self.name = None
        self.default = None
        self.mode = None
        self.filter = FileTypeFilter.empty

        self.label.hide()
        self.btn_select.hide()

    def setup(self, config: QSettings, name: str, default: Path = None,
              label: str = None, mode: str = "directory"):
        """
        Setup the link to a :py:class:`QSettings` instance
        and connect the select function to the button.

        Parameters
        ----------
        config : QSettings
            The QSettings instance, that shall be connected.
        name : str
            The key to store the state of this widget.
        default : Path, optional
            A default path. The default is None.
        label : str, optional
            The label would be shown infront of the lineEdit. The default is None.
        mode : str, optional
            Choose 'file' or 'directory' as selection mode.
            In 'file' mode a filter can be set. The default is "directory".
        """
        self.config = config
        self.name = name
        self.default = default
        self.set_mode(mode)
        self.set_label(label)

        self.load_value()
        self.lineEdit.editingFinished.connect(self.collect)
        self.btn_select.show()
        self.btn_select.clicked.connect(self.select_path)

    def set_label(self, label: str = None):
        """ set the label of the widget."""
        if label:
            self.label.show()
            self.label.setText(label)
        else:
            self.label.hide()

    def set_mode(self, mode: str = "directory",
                 filetypfilter: FileTypeFilter = FileTypeFilter.empty):
        """
        Set the selection mode of the widget. When choosing 'file', a filter can be set.

        Parameters
        ----------
        mode : str, optional
            Select "directory" or "file". The default is "directory".
        filetypfilter : FileTypeFilter, optional
            Choos a filter. The default is FileTypeFilter.empty.
        """
        if mode not in (modes := ("file", "directory")):
            self.logger.error(f"mode '{mode}' not supported, only {modes}")
        self.mode = mode
        self.set_filter(filetypfilter)

    def set_icon(self, icon):
        if isinstance(icon, str):
            icon = QIcon(icon)
        self.btn_select.setIcon(icon)

    def set_filter(self, filetypfilter: FileTypeFilter = FileTypeFilter.empty):
        """ Manualy set the filter of the widget."""
        if isinstance(filetypfilter, str) and filetypfilter in (f.name for f in FileTypeFilter):
            filetypfilter = FileTypeFilter[filetypfilter]
        if isinstance(filetypfilter, FileTypeFilter):
            self.filter = filetypfilter

    def set_value(self, path: Path) -> Path | None:
        """ set a path to be stored. "None" is a valid parameter as well as return value."""
        self.logger.debug(f"set {path=}")
        if path is None:
            return self.reset_value()

        # TODO: color for non valid path
        if not path.exists():
            self.logger.warning(f"'{path}' doesnt exists")
        elif self.mode == "file" and not path.is_file():
            self.logger.warning(f"'{path}' is not a file")
        elif self.mode == "directory" and not path.is_dir():
            self.logger.warning(f"'{path}' is not a directory")
        else:   # path is valid

            path = path.resolve()
            self.config.setValue(self.name, str(path))

        self.lineEdit.setText(str(path))
        return path

    def reset_value(self) -> None:
        """ reset the stored path to 'None'."""
        self.logger.debug("path not set")
        self.config.setValue(self.name, "")
        self.lineEdit.setText("<NONE>")
        return None

    def load_value(self) -> Path | None:
        """ load the stored path. If no valid value is stored the widget resets."""
        val = self.config.value(self.name, type=str, defaultValue=self.default)
        self.logger.info(f"load {self.name}={val}")

        if val == "":
            return self.reset_value()
        if not Path(val).exists():
            self.logger.info("stored path was invalid. reset")
            return self.reset_value()
        return self.set_value(Path(val))

    def collect(self) -> Path | None:
        """ save the wiget state."""
        val = self.lineEdit.text()
        if val == "":
            return self.reset_value()
        return self.set_value(Path(val))

    def select_path(self) -> Path:
        """ open a :py:class:`QFileDialog` to select a path."""
        path = Path.home() if (path := self.load_value()) is None else path
        options = dict(directory=str(path))
        if self.mode == "directory":
            options["caption"] = "select directory"
            path = QFileDialog.getExistingDirectory(self, **options)
        elif self.mode == "file":
            options["caption"] = f"select{' '+self.filter.name if self.filter else ''} file"
            options["filter"] = self.filter.filter_str
            path, f = QFileDialog.getOpenFileName(self, **options)
        else:
            self.logger.error("mode not set, selection not possible")
            return None

        if path != "":
            return self.set_value(Path(path))
        self.logger.info("selection canceld.")
