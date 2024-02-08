# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:47:01 2024

@author: kolja
"""

import pytest
from PyQt5.QtCore import QSettings
import logging

@pytest.fixture
def config():
    config = QSettings("k.wagner", "configwidgets/test")
    config.clear()
    yield config
    config.clear()
