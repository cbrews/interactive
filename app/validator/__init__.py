from abc import ABCMeta

def factory(type):
    pass

class Base_Lock_Validator:
    __metaclass__ = ABCMeta

    def __init__(true_value, additional_data):
        self.true_value = true_value
        self.additional_data = additional_data

    def beforeValidate(self, test_payload):
        pass

    def afterValidate(self, test_payload):
        pass

    def do_validate(self, test_payload):
        self.beforeValidate(test_payload)
        result = self.validate(test_payload)
        self.afterValidate(test_payload)

        return result

    def validate(self, test_payload):
        raise NotImplementedError("${self.__class__.__name__}.validate() has not been implemented")
