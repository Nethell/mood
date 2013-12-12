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
    """Document of a users' stories
    Fields:
    - user: The one who posts this story
    - scenery: The scenery of this story
    - tags: Tags attached on this story
    - content: The content of this story
    - post_time: The time when this story be posted
    """

    __collection__ = "stories"

    structure = {
        'user': ObjectId,
        'scenery': ObjectId,
        'tags': [basestring],
        'content': basestring,
        'post_time': datetime.datetime
    }

    required = ['user', 'scenery', 'tags', 'content', 'post_time']

    use_autorefs = True
