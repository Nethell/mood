# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""The model of stories"""

import datetime
from bson import ObjectId
from mood.models import conn
from mood.models import BaseDoc


@conn.register
class Story(BaseDoc):
    """Document of a users' stories"""

    __collection__ = "stories"

    structure = {
        'user_id': ObjectId,
        'scenery_id': ObjectId,
        'content': basestring,
        'brief': basestring,
        'post_time': datetime.datetime,
        'count': {
            'up': int,
        },
        'classify': basestring,  # decide by machine or human?
    }

    default_values = {
        'post_time': datetime.datetime.utcnow,
        'count.up': 0,
    }

    required = ['user_id', 'scenery_id', 'content']
