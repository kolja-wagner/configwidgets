# -*- coding: utf-8 -*-
"""
Testing configwidgets.containers

@author: kolja
"""

import pytest
from PyQt5.QtCore import QSettings

from configwidgets import ConfigGroupBox, ConfigNotSetupError


def test_checkbox(qtbot, config):
    assert config.value("pytest/groupbox", type=bool) == False

    # setup doesnt change config
    widget = ConfigGroupBox()
    val = widget.isChecked()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(not val)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.isChecked() == val
    
    
    widget.setup(config, "pytest/groupbox", default=True, toggle_visibility=False)
    assert config.value("pytest/groupbox", type=bool) == False

    # collect does change config
    assert widget.collect() == True
    assert config.value("pytest/groupbox", type=bool) == True

    # set value change config
    widget.set_value(False)
    assert config.value("pytest/groupbox", type=bool) == False

    # toggle activates collect
    widget.setChecked(True)
    assert config.value("pytest/groupbox", type=bool) == True