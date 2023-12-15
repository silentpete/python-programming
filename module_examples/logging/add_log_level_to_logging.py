#!/usr/bin/env python3
"""
How to add logging level to the logging library.
Reference: https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility
"""

# Import Internal Libraries
import argparse
import logging

DESCRIPTION = """\
  This is the description...
"""

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=DESCRIPTION
)
parser.add_argument(
    "--log-level", default="INFO",
    help="log levels: TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL")
p_args = parser.parse_args()

# set log level of logging module
print(f"--log-level={p_args.log_level}")
# TRACE=5
# DEBUG=10
# INFO=20
# WARN=30
# ERROR=40
# CRITICAL=50

TRACE_LOG_LEVEL_NUM = logging.DEBUG - 5
logging.addLevelName(TRACE_LOG_LEVEL_NUM, 'TRACE')
def trace(self, message, *args, **kws):
    '''
    something
    '''
    if self.isEnabledFor(TRACE_LOG_LEVEL_NUM):
        # Yes, logger takes its '*args' as 'args'.
        self.log(TRACE_LOG_LEVEL_NUM, message, *args, **kws)

logging.Logger.trace = trace

numeric_level = getattr(logging, p_args.log_level.upper(), None)
print(f"numeric_level={numeric_level}")
logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')

logging = logging.getLogger()
logging.trace("tracing")
logging.debug("debuging")
logging.info("information")
logging.warning("warnings")
logging.error("errors")
logging.critical("criticals")
