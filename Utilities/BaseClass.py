import inspect
import logging

import pytest
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Check if logger already has handlers to avoid duplicate logs
        if not logger.handlers:
            # If no handlers are present, create a new handler
            consoleHandler = logging.StreamHandler()  # This handler will output to the console
            fileHandler = logging.FileHandler('logfile.1')

            formatter = logging.Formatter("%(asctime)s: %(levelname)s:%(name)s: %(message)s")
            consoleHandler.setFormatter(formatter)
            fileHandler.setFormatter(formatter)

            logger.addHandler(consoleHandler)
            logger.addHandler(fileHandler)

            logger.setLevel(logging.INFO)

        return logger
