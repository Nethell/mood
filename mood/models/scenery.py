# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

from bson import ObjectId
from mood.models import conn
from mood.models import BaseDoc


@conn.register
class Scenery(BaseDoc):
    """Document of a stoies' sceneries"""

    __collection__ = "sceneries"

    structure = {
        'name': basestring,
        'story_id': ObjectId,
        'url': basestring
    }

    required_fields = ['story_id', 'url', 'name']
