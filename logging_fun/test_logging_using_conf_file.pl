#!/usr/bin/env python

import os, sys
import logging
import logging.config
import myclasses.ClassA as classA

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if len(sys.argv) > 1:
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    logger.info("using config file for logging configuration")


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

# create classA object
cA = classA.ClassA()


