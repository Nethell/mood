# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""This module gives the Exception and code."""

CODE_UNKNOWN_EXC = (1, u'Unknown error.')

#USER
CODE_USER_NOT_FOUND = (1100, u'Not such a user.')
CODE_USER_NOT_LOGIN = (1101, u'User not login.')
CODE_USER_PASSWD_TOO_SHORT = (1102, u'Password too short(at least 6)')
CODE_USER_PASSWD_TOO_LONG = (1103, u'Password too long(at most 30)')
CODE_USER_PASSWD_WRONG_FORMAT = (1104, u'Invalid characters in password')
CODE_USER_BAD_EMAIL = (1105, u'Invalid email address')
CODE_USER_FIELD_VALIDATE_EXC = (1106, u'User feilds in db validate error.')


class BadMoodExc(Exception):

    def __init__(self, code=CODE_UNKNOWN_EXC, detail=None):
        assert code
        self.code = code[0]
        self.msg = code[1] + detail.decode("utf8") if detail else code[1]

    def __str__(self):
        return self.msg.encode('utf8')
