# -*- coding: utf-8 -*-
"""
Testing the code in `configwidgets.buttons`

@author: kolja
"""
from configwidgets import ConfigCheckBox, ConfigRadioButton
from PyQt5.QtCore import QSettings

def test_checkbox(qtbot, config):
    assert config.value("pytest/checkbox", type=bool) == False

    # setup doesnt change config
    widget = ConfigCheckBox()
    val = widget.isChecked()
    assert widget.load_value() is None
    assert widget.isChecked() == val
    assert widget.set_value(not val) is None
    assert widget.collect() is None
    assert widget.isChecked() == val
    
    
    widget.setup(config, "pytest/checkbox", default=True)
    assert config.value("pytest/checkbox", type=bool) == False

    # collect does change config
    assert widget.collect() == True
    assert config.value("pytest/checkbox", type=bool) == True

    # set value change config
    widget.set_value(False)
    assert config.value("pytest/checkbox", type=bool) == False

    # toggle activates collect
    widget.toggle()
    assert config.value("pytest/checkbox", type=bool) == True
    


def test_radio(qtbot, config):
    config.setValue("pytest/radio1", True)
    config.setValue("pytest/radio2", False)
    
    # initialize doesnt change
    widget1 = ConfigRadioButton()
    widget2 = ConfigRadioButton()
    v1, v2 = widget1.isChecked(), widget2.isChecked()
    assert widget1.load_value() is None
    assert widget1.isChecked() == v1
    assert widget2.isChecked() == v2

    assert widget1.set_value(not v1) is None
    assert widget1.isChecked() == v1
    assert widget2.isChecked() == v2

    assert widget1.collect() is None
    assert not widget1.isChecked()
    assert not widget2.isChecked()
    
    # load values work correctly
    widget1.setup(config, "pytest/radio1", default=False)
    widget2.setup(config, "pytest/radio2", default=False)
    assert widget1.isChecked() == config.value("pytest/radio1", type=bool)
    assert widget2.isChecked() == config.value("pytest/radio2", type=bool)
    assert widget1.isChecked()
    
    # click  triggers collect
    widget2.click()
    assert widget1.isChecked() == config.value("pytest/radio1", type=bool)
    assert widget2.isChecked() == config.value("pytest/radio2", type=bool)
    assert widget2.isChecked()

    # set_value works correctly
    widget1.set_value(True)
    assert widget1.isChecked() == config.value("pytest/radio1", type=bool)
    assert widget2.isChecked() == config.value("pytest/radio2", type=bool)
    assert widget1.isChecked()

    
    
    