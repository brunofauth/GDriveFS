import os
import logging
import logging.handlers

import gdrivefs.config

logger = logging.getLogger()

def configure(is_debug=gdrivefs.config.IS_DEBUG):
    if is_debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    def _configure_syslog():
        facility = logging.handlers.SysLogHandler.LOG_LOCAL0
        sh = logging.handlers.SysLogHandler(facility=facility)
        formatter = logging.Formatter('GD: %(name)-12s %(levelname)-7s %(message)s')
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    def _configure_console():
        sh = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s')
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    if is_debug is True:
        _configure_console()
    else:
        _configure_syslog()
