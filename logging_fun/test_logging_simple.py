#!/usr/bin/env python

import os, sys
import logging
import myclasses.ClassA as classA

#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
#logger.addHandler(ch)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

# create classA object
cA = classA.ClassA()


