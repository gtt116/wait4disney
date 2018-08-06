import logging


def setup_logging():
    logging.BASIC_FORMAT = "%(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(format='[%(asctime)s] ' + logging.BASIC_FORMAT)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
