# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:47:01 2024

@author: kolja
"""

import logging

import pytest
from PyQt5.QtCore import QSettings


@pytest.fixture
def config():
    config = QSettings("k.wagner", "configwidgets")
    config.clear()
    yield config
    config.clear()
