#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os, sys, re
import logging
import logging.config
import argparse
import myclasses.ClassA as classA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

 
def main():

    parser = argparse.ArgumentParser(description="testing logging using different conf files")
    
    parser.add_argument("--conf", dest="conf", type=str, default=None, required=False, help="config file")
    
    args = parser.parse_args()

    if args.conf:
        logging.config.fileConfig(args.conf, disable_existing_loggers=False)
        logger.info("using config file %s for logging configuration" % args.conf)


    # 'application' code
    print("\nApp code:\n")
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    # create classA object
    print("\nLib code:\n")
    cA = classA.ClassA()

    sys.exit(0)

 
####################
 
if __name__ == "__main__":
    main()
