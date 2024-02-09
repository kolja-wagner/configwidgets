# -*- coding: utf-8 -*-
"""
Testing configwidgets.datetime

@author: kolja
"""
from datetime import date, datetime, time, timedelta

import pytest

from configwidgets import (ConfigDateEdit, ConfigDateTimeEdit,
                           ConfigNotSetupError, ConfigTimeEdit)


def test_datetime(qtbot, config):
    # assert config.value("pytest/datetime", type=datetime)==None

    # init doesnt change config
    widget = ConfigDateTimeEdit()
    val = widget.dateTime().toPyDateTime()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(not val)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.dateTime().toPyDateTime() == val
    
    # # define values
    v1 = datetime.utcnow().replace(microsecond=0)
    v2 = datetime.utcnow().replace(year=2022, microsecond=0)
    
    # # default config == now
    widget.setup(config, "pytest/datetime", default = None)
    assert (widget.default - v1) < timedelta(seconds=1)
    
    # # setup doesnt alter config
    widget.setup(config, "pytest/datetime", default = v1)
    assert config.value("pytest/datetime") == None
    
    # # collect does change config
    assert widget.collect() == v1
    assert config.value("pytest/datetime", type=datetime) == v1

    # # set value change config
    widget.set_value(v2)
    assert config.value("pytest/datetime", type=datetime) == v2

    # # editing activates collect
    widget.setDateTime(v1)
    widget.editingFinished.emit()
    assert config.value("pytest/datetime", type=datetime) == v1

def test_date(qtbot, config):
    # assert config.value("pytest/date", type=date) == None

    # init doesnt change config
    widget = ConfigDateEdit()
    val = widget.date().toPyDate()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(not val)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.date().toPyDate() == val
    
    # # define values
    v1 = datetime.utcnow().date()
    v2 = datetime.utcnow().date().replace(year=2022)
    
    # # default config == now
    widget.setup(config, "pytest/date", default = None)
    assert (widget.default == v1)
    
    # # setup doesnt alter config
    widget.setup(config, "pytest/date", default = v1)
    assert config.value("pytest/date") == None
    
    # # collect does change config
    assert widget.collect() == v1
    assert config.value("pytest/date", type=date) == v1

    # # set value change config
    widget.set_value(v2)
    assert config.value("pytest/date", type=date) == v2

    # # editing activates collect
    widget.setDate(v1)
    widget.editingFinished.emit()
    assert config.value("pytest/date", type=date) == v1


def test_time(qtbot, config):
    # assert config.value("pytest/time", type=time) == None

    # init doesnt change config
    widget = ConfigTimeEdit()
    val = widget.time().toPyTime()
    with pytest.raises(ConfigNotSetupError):
        widget.load_value()
    with pytest.raises(ConfigNotSetupError):
        widget.set_value(not val)
    with pytest.raises(ConfigNotSetupError):
        widget.collect()
    assert widget.time().toPyTime() == val
    
    # # define values
    v1 = datetime.utcnow().time().replace(microsecond=0)
    v2 = datetime.utcnow().time().replace(hour=2, microsecond=0)
    
    # # default config == now
    widget.setup(config, "pytest/time", default = None)
    assert (widget.default.replace(microsecond=0) == v1)
    
    # # setup doesnt alter config
    widget.setup(config, "pytest/time", default = v1)
    assert config.value("pytest/time") == None
    
    # # collect does change config
    assert widget.collect() == v1
    assert config.value("pytest/time", type=time) == v1

    # # set value change config
    widget.set_value(v2)
    assert config.value("pytest/time", type=time) == v2

    # # editing activates collect
    widget.setTime(v1)
    widget.editingFinished.emit()
    assert config.value("pytest/time", type=time) == v1

    
    
