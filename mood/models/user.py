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


ID_MIN = 4                      # Should these be put in consts.py?
ID_MAX = 32
PSWD_MIN = 6
PSWD_MAX = 20
MAIL_MIN = 6                    # I don't know why:(
MAIL_MAX = 320                  # 254(RFC5321)
ID_RE = re.compile('^\w[A-Za-z0-9_]*')
PSWD_RE = re.compile('^[\S]*')
MAIL_RE = re.compile('^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$', re.IGNORECASE)


class field_validator(object):
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

    Fields:
    - account_id: Id of a user
    - account_pswd: Password of a user
    - account_mail: Email of a user
    - nick: Nickname of a user
    - sex: Female or Male or something else?
    - desc: Description of a user
    - tags: Tags of a user
    - addr: Address of a user
    - reg_time: Time when a user registers
    """

    __collection__ = "users"

    structure = {
        'account_id': basestring,
        'account_pswd': basestring,
        'account_mail': basestring,
        'nick': basestring,
        'sex': basestring,
        'desc': basestring,
        'tags': [basestring],
        'addr': basestring,
        'reg_time': datetime.datetime
    }
    validators = {        # Validators of some fields of this Document
        'account_id': field_validator(ID_MIN, ID_MAX, ID_RE),
        'account_pswd': field_validator(PSWD_MIN, PSWD_MAX, PSWD_RE),
        'account_mail': field_validator(MAIL_MIN, MAIL_MAX, MAIL_RE)
    }
