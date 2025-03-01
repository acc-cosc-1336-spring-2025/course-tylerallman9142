#

import datetime


def get_hour(epoch_seconds):
    dt_object = datetime.datetime.fromtimestamp(epoch_seconds)
    return dt_object.hour

def get_minutes(epoch_seconds):
    dt_object = datetime.datetime.fromtimestamp(epoch_seconds)
    return dt_object.minute

def get_seconds(epoch_seconds):
    dt_object = datetime.datetime.fromtimestamp(epoch_seconds)
    return dt_object.second