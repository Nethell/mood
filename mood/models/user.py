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
import logging
from mood.consts import (
    USER_AUTHORITY_HUMAN, USER_DEFAULT_DESC,
)
from mood.models import conn
from mood.models import BaseDoc
from mood.exceptions import BadMoodExc
from mood.consts import (
    USER_PSWD_MIN,USER_PSWD_MAX,
)
from mood.exceptions import (
    CODE_USER_PASSWD_TOO_SHORT,
    CODE_USER_PASSWD_TOO_LONG,
    CODE_USER_PASSWD_WRONG_FORMAT,
    CODE_USER_BAD_EMAIL,
    CODE_USER_FIELD_VALIDATE_EXC,
)


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
        if self.formats == PSWD_RE:
            if len(value) < self.min_len:
                raise BadMoodExc(CODE_USER_PASSWD_TOO_SHORT)
            elif len(value) > self.max_len:
                raise BadMoodExc(CODE_USER_PASSWD_TOO_LONG)
            elif not self.formats.match(value):
                raise BadMoodExc(CODE_USER_PASSWD_WRONG_FORMAT)
            else:
                return True

        elif self.formats == MAIL_RE:
            if len(value) >= self.min_len and \
               len(value) <= self.max_len and \
               self.formats.match(value):
                return True
            else:
                raise BadMoodExc(CODE_USER_BAD_EMAIL)
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
        'nickname': basestring,
        'sex': int,
        'desc': basestring,
        'medals': [basestring],  # like: 点赞狂魔，发帖狂魔
        'rep': int,              # reputation, 经验值
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
        'authority': int,
        'avatar': {
            'big': basestring,
            'small': basestring
        }
    }

    required_fields = ['passwd', 'email', 'nickname', 'sex']

    default_values = {
        'reg_time': datetime.datetime.utcnow,
        'desc': USER_DEFAULT_DESC,
        'rep': 1,
        'authority': USER_AUTHORITY_HUMAN,
        'count.stories_passed': 0,
        'count.stories_denied': 0,
        'count.sceneries_passed': 0,
        'count.sceneries_denied': 0,
        'count.comments_passed': 0,
        'count.comments_denied': 0,
    }

    validators = {        # Validators of some fields of this Document
        'passwd': FieldValidator(USER_PSWD_MIN, USER_PSWD_MAX, PSWD_RE),
        'email': FieldValidator(MAIL_MIN, MAIL_MAX, MAIL_RE)
    }


logger = logging.getLogger('mood.models')


# NOTE: not validate params!!!!
def create_user(**kwargs):
    user = conn.User()
    user['nickname'] = kwargs.get('nickname')
    user['passwd'] = kwargs.get('passwd')
    user['email'] = kwargs.get('email')
    user['sex'] = kwargs.get('sex')
    user.save()
    logger.debug("(create_user): {0} become a human".format(user['nickname']))


def update_user_authority(self, authority):
    pass
