import pkgutil
import string
from abc import ABCMeta
from pprint import pprint

class Base_Lock_Validator:
    __metaclass__ = ABCMeta

    def __init__(true_value=None, additional_data=None):
        self.true_value = true_value
        self.additional_data = additional_data

    def beforeValidate(self, payload=None):
        pass

    def afterValidate(self, payload=None):
        pass

    def do_validate(self, payload=None):
        self.beforeValidate(test_payload)
        result = self.validate(test_payload)
        self.afterValidate(test_payload)

        return result

    def validate(self, payload=None):
        raise NotImplementedError("${self.__class__.__name__}.validate() has not been implemented")

import importlib

class Factory:

    modules = None

    def __init__(self, path, name, class_prefix=None, class_suffix=None, class_separator="_"):
        self.path = path
        self.name = name

        print self.path
        print self.name

        self.class_prefix = class_prefix
        self.class_suffix = class_suffix
        self.class_separator = class_separator

    def create(self, key):
        modules = self.get_modules()

        if not key in modules.keys():
            return None # raise exception instead?

        kls = self.import_class(modules[key])

        print kls


        return

    def import_class(self, module):
        return importlib.import_module("." + module[0], self.name)

    def get_keys(self):
        return self.get_modules().keys()

    def get_modules(self):
        if not self.modules:
            self.modules = {}
            for loader, name, is_pkg in pkgutil.iter_modules(__name__):
                print (loader, name, is_pkg)
                if not is_pkg:
                    self.modules[name] = (name, self.classname(name))

        return self.modules

    def classname(self, module):
        if self.class_prefix:
            module = self.class_prefix + self.class_separator + module

        if self.class_suffix:
            module = module + self.class_separator + self.class_suffix

        return string.capwords(module, self.class_separator)

f = Factory(__path__, __name__, class_prefix="validator")
