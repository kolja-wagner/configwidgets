# -*- coding: utf-8 -*-
"""
Defining custom errors

@author: kolja
"""


class ConfigNotSetupError(Exception):
    """ Exception raised, if a ConfigWidget-Method (load_value/set_value/collect)
    is called without beeing setup)."""
    def __init__(self, obj):
        self.obj = obj
        name = f"{obj.name} " if hasattr(obj, "name") and obj.name is not None else ""
        super().__init__(f"Widget {name}of type={type(obj)} was not setup.")
