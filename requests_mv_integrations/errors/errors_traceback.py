#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import sys
import traceback


def get_exception_message(ex):
    """Build exception message with details.
    """
    template = "{0}: {1!r}"
    return template.format(type(ex).__name__, ex.args)


def print_traceback(ex):
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb)


def print_limited_traceback(ex, limit=1):
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exc(limit=1, file=sys.stdout)