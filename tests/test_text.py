# -*- coding: utf-8 -*-
"""
Testing the code in `configwidgets.text`

@author: kolja
"""

import pytest
from PyQt5.QtCore import QSettings

from configwidgets import (ConfigComboBox, ConfigLineEdit, ConfigNotSetupError,
                           ConfigPlainTextEdit)


def test_lineedit(qtbot, config):
    assert config.value("pytest/lineedit", type=int) == 0

    # without setup no values
    widget = ConfigLineEdit()
    val = widget.text()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(5)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.text() == val

    # setup doesnt change state    
    widget.setup(config, "pytest/lineedit", default="a")
    assert config.value("pytest/lineedit", type=str) == ""
    assert widget.text() == "a"
    
    # # collect changes state
    assert widget.collect() == "a" 
    assert config.value("pytest/lineedit", type=str) == "a"
    assert widget.text() == "a"
    
    # # set value changes state
    assert widget.set_value("b") == "b"
    assert config.value("pytest/lineedit", type=str) == "b"
    assert widget.text() == "b"
    
    # # load value updates
    config.setValue("pytest/lineedit", "c")
    assert widget.load_value() == "c"
    assert widget.text() == "c"

def test_combobox(qtbot, config):
    assert config.value("pytest/combo", type=int) == 0

    # without setup no values
    widget = ConfigComboBox()
    val = widget.currentText()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value("a")
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.currentText() == val

    # setup doesnt change state    
    widget.setup(config, "pytest/combo", items=("a","b","c"))
    assert config.value("pytest/combo", type=str) == ""
    assert widget.currentText() == "a" # default = first item if not specified
    
    # # collect changes state
    assert widget.collect() == "a" 
    assert config.value("pytest/combo", type=str) == "a"
    assert widget.currentText() == "a"
    
    # # set value changes state
    assert widget.set_value("b") == "b"
    assert config.value("pytest/combo", type=str) == "b"
    assert widget.currentText() == "b"
    
    # # load value updates
    config.setValue("pytest/combo", "c")
    assert widget.load_value() == "c"
    assert widget.currentText() == "c"
    
def test_plainedit(qtbot, config):
    assert config.value("pytest/plainedit", type=int) == 0

    # without setup no values
    widget = ConfigPlainTextEdit()
    val = widget.toPlainText()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(5)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.toPlainText() == val

    # setup doesnt change state    
    widget.setup(config, "pytest/plainedit", default="a")
    assert config.value("pytest/plainedit", type=str) == ""
    assert widget.toPlainText() == "a"
    
    # # collect changes state
    assert widget.collect() == "a" 
    assert config.value("pytest/plainedit", type=str) == "a"
    assert widget.toPlainText() == "a"
    
    # # set value changes state
    assert widget.set_value("b") == "b"
    assert config.value("pytest/plainedit", type=str) == "b"
    assert widget.toPlainText() == "b"
    
    # # load value updates
    config.setValue("pytest/plainedit", "c")
    assert widget.load_value() == "c"
    assert widget.toPlainText() == "c"
    
def test_plainedit_autocollect(qtbot, config):
    widget = ConfigPlainTextEdit()
    widget.setup(config, "pytest/plainedit", default="a", autocollect=False)
    qtbot.keyPress(widget, "c")
    assert widget.toPlainText() == "ca"
    assert config.value("pytest/plainedit", type=str) == ""
    
    widget.setup(config, "pytest/plainedit", default="a", autocollect=True)
    qtbot.keyPress(widget, "c")
    assert widget.toPlainText() == "ca"
    assert config.value("pytest/plainedit", type=str) == "ca"

