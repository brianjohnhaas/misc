#!/usr/bin/env python

import os, sys
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler()) # just in case

class ClassA(object):

    def __init__(self):
        print("Testing logger for ClassA creation:")
        logger.debug("--debug: creating ClassA obj")
        logger.info("--info: creating ClassA obj")
        logger.warn("--warning: creating ClassA obj")
        logger.error("--error: creating ClassA obj")
        logger.critical("critical: creating ClassA obj")

