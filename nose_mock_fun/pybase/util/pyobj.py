#!/usr/bin/env python

import sys, os, re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('pyobj_logger')

class PyObj(object):

    def __init__(self):
        self.val = 1

    def get_file_contents(self, filename):
        text = ""
        for line in open(filename):
            text += line
        return(text)


    def get_file_contents_via_context_manager(self, filename):
        text = ""
        with open(filename) as o:
            for line in o:
                text += line
        return(text)


