# -*- coding: utf-8 -*-

import logging

models_logger = logging.getLogger('models')
models_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | [%(name)s] | %(levelname)s: %(message)s')

ch.setFormatter(formatter)

models_logger.addHandler(ch)

# logger switch on
models_logger.propagate = True
# logger switch off
# logger.propagate = False
