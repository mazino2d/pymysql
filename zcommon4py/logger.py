import logging
import os


class Logger(object):
    def __init__(self, name="logger", level=logging.DEBUG):
        FORMAT = "[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s"

        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter(FORMAT))

        os.makedirs("log", exist_ok=True)
        fh = logging.FileHandler("log/%s.log" % name, "a")
        fh.setFormatter(logging.Formatter(FORMAT))

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        while self.logger.hasHandlers():
            self.logger.removeHandler(self.logger.handlers[0])

        self.logger.addHandler(fh)

        self.info("--- --- --- --- Logger is started! --- --- --- ---")

        self.logger.addHandler(sh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)


if __name__ == "__main__":
    logger = Logger()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
