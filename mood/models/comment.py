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
    """Document of a users' comments
    Fields:
    - user: The one who posts this comment
    - story: The story this comment follow
    - content: The content of this comment
    - post_time: The time when this comment be posted
    """

    __collection__ = "comments"

    structure = {
        'user': ObjectId,
        'story': ObjectId,
        'content': basestring,
        'post_time': datetime.datetime
    }

    required = ['user', 'story', 'content', 'post_time']

    use_autorefs = True
