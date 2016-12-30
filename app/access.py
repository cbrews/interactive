import dates
from pprint import pprint

PASSWORD = 'pw'
GEOLOCATION = 'coords'
START_TIME = 'start'
GLOBAL = 'enabled'

'''
@param locks dictionary
@param keys dictionary
@return bool
'''
def validate(locks, keys):
    for lock in locks:
        access = access_factory(lock, locks[lock])

        if lock in keys.keys():
            test_value = keys[lock]
        else:
            test_value = ''

        if not access.validate(test_value):
            return False
    return True


def access_factory(lock, value):
    if(lock == PASSWORD):
        return PasswordAccess(value)
    elif(lock == GLOBAL):
        return GlobalAccess(value)
    elif(lock == GEOLOCATION):
        return GeoAccess(value)
    elif(lock == START_TIME):
        return TimeAccess(value)
    else:
        raise KeyError("Error in AccessFactory: lock type \"" + lock + "\" for access validation does not exist.")

class AbstractAccess:
    def __init__(self, value):
        self.value = value

class GlobalAccess(AbstractAccess):
    # Returns enabled value (true/false)
    def validate(self, test):
        return True if self.value else False

class PasswordAccess(AbstractAccess):
    def validate(self, test):
        return self.value == test

class GeoAccess(AbstractAccess):
    # @TODO
    def validate(self, test):
        return True

class TimeAccess(AbstractAccess):
    def __init__(self, value):
        self.value = dates.str_to_obj(value)

    def validate(self, test):
        return dates.now() >= self.value
        