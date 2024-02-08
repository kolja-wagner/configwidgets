# -*- coding: utf-8 -*-
"""
Testing the code in `configwidgets.numbers`

@author: kolja
"""

from PyQt5.QtCore import QSettings
import pytest 

from configwidgets import ConfigSpinBox, ConfigDoubleSpinBox, ConfigNotSetupError



def test_spinbox(qtbot, config):
    assert config.value("pytest/spinbox", type=int) == 0

    # without setup no values
    widget = ConfigSpinBox()
    val = widget.value()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(5)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.value() == val

    # setup doesnt change state    
    widget.setup(config, "pytest/spinbox", default=5)
    assert config.value("pytest/spinbox", type=int) == 0
    assert widget.value() == 5
    
    # collect changes state
    assert widget.collect() == 5 
    assert config.value("pytest/spinbox", type=int) == 5 
    assert widget.value() == 5
    
    # set value changes state
    assert widget.set_value(10) == 10
    assert config.value("pytest/spinbox", type=int) == 10
    assert widget.value() == 10
    
    # load value updates
    config.setValue("pytest/spinbox", 20)
    assert widget.load_value() == 20
    assert widget.value() == 20
    
    
def test_doublespinbox(qtbot, config):
    assert config.value("pytest/doublespinbox", type=int) == 0

    # without setup no values
    widget = ConfigDoubleSpinBox()
    val = widget.value()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(5)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.value() == val

    # setup doesnt change state    
    widget.setup(config, "pytest/doublespinbox", default=5)
    assert config.value("pytest/doublespinbox", type=int) == 0
    assert widget.value() == 5
    
    # collect changes state
    assert widget.collect() == 5 
    assert config.value("pytest/doublespinbox", type=int) == 5 
    assert widget.value() == 5
    
    # set value changes state
    assert widget.set_value(10) == 10
    assert config.value("pytest/doublespinbox", type=int) == 10
    assert widget.value() == 10
    
    # load value updates
    config.setValue("pytest/doublespinbox", 20)
    assert widget.load_value() == 20
    assert widget.value() == 20
        