from abc import ABCMeta

def factory(type):
    pass

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
