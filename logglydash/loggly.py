import logging
from logging.handlers import SysLogHandler

def getLogger():
    logger = logging.getLogger('logglylogger')
    logger.setLevel(logging.INFO)
    syslog = SysLogHandler(address=('logs.loggly.com', 41691))
    formatter = logging.Formatter('%(levelname)s %(message)s')
    syslog.setFormatter(formatter)
    logger.addHandler(syslog)

    return logger
