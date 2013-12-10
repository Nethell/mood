# -*- coding: utf-8 -*-

#                            _    __
#                           | |  / _|
#  _ __ ___   ___   ___   __| | | |_ _ __ ___
# | '_ ` _ \ / _ \ / _ \ / _` | |  _| '_ ` _ \
# | | | | | | (_) | (_) | (_| |_| | | | | | | |
# |_| |_| |_|\___/ \___/ \__,_(_)_| |_| |_| |_|

"""The model of user's account'"""

import datetime
import re
from mongokit import Connection, Document

ID_MIN = 4                      # Should these be put in consts.py?
ID_MAX = 32
PSWD_MIN = 6
PSWD_MAX = 20
MAIL_MIN = 6                    # I don't know why:(
Mail_MAX = 320                  # 254(RFC5321)
ID_RE = re.compile('^\w[A-Za-z0-9_]*')
PSWD_RE = re.compile('^[\S]*')
MAIL_RE = re.compile('^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$',re.IGNORECASE)


def field_validator(min_len, max_len, re_obj):
    """The validator for the fields of document 'User'
    
    Arguments:
    - `min_len`: The minimum length of a field
    - `max_len`: The maximum length of a field
    - `re_obj` : The format of field
    
    Returns:
       A function validate a given value of a field 
       with 'min_len', 'max_len' and the format expressed
       by the regular object 're_obj'.
    """
    def validator(value):
        """Validate the value of a field
        
        Arguments:
        - `value`: The value of a field

        Returns:
          Return 'True' if the 'value' is correct and 'False' if not.
        """
        if len(value) >= min_len and \
           len(value) <= max_len and \
           re_obj.match(value):
            return True
        else:
            raise Exception('Wrong length or format')

        return validator
        

class User(Document):
    """Document of a user's account
    
    Fields:
    - account_id: Id of a user
    - account_pswd: Password of a user
    - account_mail: Email of a user
    - nick: Nickname of a user
    - sex: Female or Male?
    - desc: Description of a user
    - tags: Tags of a user
    - addr: Address of a user
    - reg_time: Time when a user registers
    """
    structure = {
        'account_id': basestring,
        'account_pswd': basestring,
        'account_mail': basestring,
        'nick': unicode,
        'sex': basestring,
        'desc': unicode,
        'tags': [unicode],
        'addr': unicode,
        'reg_time':datetime.datetime
    }
    validators = {        # Validators of some fields of this Document
        'account_id': field_validator(id_min, id_max, id_re),
        'account_pswd': field_validator(pswd_min, pswd_max, pswd_re)
        'account_mail': field_validator(mail_min, mail_max, mail_re)
    }
