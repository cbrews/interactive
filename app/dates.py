import dateutil.parser
import datetime

def now():
    return datetime.datetime.now()

def str_to_obj(date_str):
    return dateutil.parser.parse(date_str)

def obj_to_str(date_obj):
    return date_obj.isoformat()