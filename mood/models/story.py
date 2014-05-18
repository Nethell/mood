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

    用户顶了那些景色的文章，在redis中记录用户景物name的关系
    推荐的时候，推荐这些景色中的文章
    """

    __collection__ = "stories"

    structure = {
        'user_id': ObjectId,
        'scenery_id': ObjectId,
        'content': basestring,
        'brief': basestring,
        'post_time': datetime.datetime,
        'count': {
            'liked': int,
            'commented': int,
            'collected': int
        },
        'last_liked_by': [ObjectId]
    }

    default_values = {
        'post_time': datetime.datetime.utcnow,
        'count.collected': 0,
        'count.liked': 0,
        'count.commented': 0,
    }

    required_fields = ['user_id', 'scenery_id', 'content']
