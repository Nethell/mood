# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""This is the base class of models."""

from mongokit import Connection, Document
from mood import settings


conn = Connection(settings.MONGO_HOST, port=settings.MONGO_PORT)


class BaseDoc(Document):
    __database__ = 'mood'

# NOTE: Don't change its position unless you do know what you do.
from mood.models import comment, scenery, story, user
