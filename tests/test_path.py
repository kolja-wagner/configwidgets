# -*- coding: utf-8 -*-
"""
Testing configwidgets.path

@author: kolja
"""
import logging
import time
from pathlib import Path

import pytest

from configwidgets import ConfigNotSetupError, ConfigPathWidget


def test_path(qtbot, config):
    p = Path(".").resolve()
    config.setValue("pytest/path", str(p))

    # without setup no values
    widget = ConfigPathWidget()
    val = widget.combo.currentText()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value("a")
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    with pytest.raises(ConfigNotSetupError):
        widget.select()
    val = widget.combo.currentText()

    # loading NONE doesnt change state    
    widget.setup(config, "pytest/path", default=None, label="demo", mode=None, filetyp=None)
    assert config.value("pytest/path", type=str) == str(p)
    assert widget.combo.currentText() == str(p)

    # set value
    assert widget.set_value(p.parent) == p.parent
    assert config.value("pytest/path", type=str) == str(p.parent)

    # change triggers collect
    widget.combo.setCurrentText(".")
    widget.combo.textActivated.emit(None)
    assert config.value("pytest/path", type=str) == str(p)
    assert widget.combo.currentText() == str(p)

    # change to previous.
    widget.combo.setCurrentIndex(2)
    widget.combo.textActivated.emit(None)
    assert config.value("pytest/path", type=str) == str(p.parent)
    assert widget.combo.currentText() == str(p.parent)

    
def test_path_other(qtbot, config):
    assert config.value("pytest/path", type=str) ==  ""

    # load None
    widget = ConfigPathWidget()
    widget.setup(config, "pytest/path", default=None, label=None, mode=None, filetyp=None)
    assert widget.combo.currentText() == "<NOT SET>"
    assert widget.load_value() is None
    
    # test label hidden
    assert widget.label.isHidden()
    
    widget.combo.lineEdit().setText("_this_doesnt_exists_")
    widget.combo.textActivated.emit(None)
    assert config.value("pytest/path", type=str) ==  ""
    assert widget.combo.currentText() == "_this_doesnt_exists_"
    assert widget.collect() == None
    
    
def test_path_select(qtbot, config):
    logging.error("not implemented")
    assert False
    
