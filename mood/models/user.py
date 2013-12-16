# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""The model of users' account"""

import datetime
import re
from mood.models import conn
from mood.models import BaseDoc
from mood.exceptions import BadMoodExc
from mood.exceptions import CODE_USER_FIELD_VALIDATE_EXC


PSWD_MIN = 6
PSWD_MAX = 20
MAIL_MIN = 6                    # I don't know why:(
MAIL_MAX = 320                  # 254(RFC5321)
PSWD_RE = re.compile(r'^[\S]*')
MAIL_RE = re.compile(r'^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$', re.IGNORECASE)


class FieldValidator(object):
    """The validator for fields of document 'User'
    From example of mongokit wiki
    """
    def __init__(self, min_len, max_len, re_obj):
        self.min_len = min_len
        self.max_len = max_len
        self.formats = re_obj

    def __call__(self, value):
        if len(value) >= self.min_len and \
           len(value) <= self.max_len and \
           self.formats.match(value):
            return True
        else:
            raise BadMoodExc(CODE_USER_FIELD_VALIDATE_EXC)


@conn.register
class User(BaseDoc):
    """Document of a user's account

    TODO(crow): add some indexes according to queries
    """

    __collection__ = "users"

    structure = {
        'passwd': basestring,
        'email': basestring,
        'nickname': basestring,  # NOTE(@linusp): there is no word called 'nick'
        'sex': basestring,  # m: male, f: female
        'desc': basestring,
        'medals': [basestring],  # like: 点赞狂魔，发帖狂魔
        'rep': basestring,  # reputation, 经验值
        'addr': [
            {
                'context': basestring,
                'loc': [float, float]
            }
        ],
        'reg_time': datetime.datetime,
        'count': {
            'stories_passed': int,
            'stories_denied': int,
            'sceneries_passed': int,
            'sceneries_denied': int,
            'comments_passed': int,
            'comments_denied': int,
        },
        'authority': basestring,  # g: god(admin), h: human(user), b: bug(banned)
        'avatar': {
            'big': basestring,
            'small': basestring
        }
    }

    required = ['password', 'email', 'nick']

    default_values = {
        'reg_time': datetime.datetime.utcnow,
        'authority': 'h',
        'count.stories_passed': 0,
        'count.stories_denied': 0,
        'count.sceneries_passed': 0,
        'count.sceneries_denied': 0,
        'count.comments_passed': 0,
        'count.comments_denied': 0,
    }

    validators = {        # Validators of some fields of this Document
        'password': FieldValidator(PSWD_MIN, PSWD_MAX, PSWD_RE),
        'mail': FieldValidator(MAIL_MIN, MAIL_MAX, MAIL_RE)
    }
