import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logging():
    LOG_FILE = "/home/ubuntu/wait4disney/disney.log"

    log_format = "%(asctime)s %(levelname)s [%(name)s] - %(message)s"
    logging.basicConfig(format=log_format)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    th = TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=30)
    th.setFormatter(logging.Formatter(log_format))
    root.addHandler(th)
