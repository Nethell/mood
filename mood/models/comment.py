# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""The model of comments"""

import datetime
from bson import ObjectId
from mood.models import conn
from mood.models import BaseDoc


@conn.register
class Comment(BaseDoc):
    """Document of a users' comments"""

    __collection__ = "comments"

    structure = {
        'user_id': ObjectId,
        # NOTE: image_url should contain into this in some specific structure
        'content': basestring,
        'post_time': datetime.datetime,
        'target': {
            'type': basestring,  # story or comment
            'id': ObjectId
        }
    }

    default_values = {
        'post_time': datetime.datetime.utcnow
    }

    required = ['user_id', 'target', 'content']
