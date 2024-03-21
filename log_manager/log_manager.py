# log_manager/log_manager.py

"""This module allows the user to make log operations.

Examples:

    >>> from log_manager.log_manager import LogManager
    >>> log_manager = LogManager()

    >>> log_manager.info("This is an informational message.")
    >>> log_manager.error("An error occurred!")
    >>> log_manager.debug("This is just an informational message.")
    >>> log_manager.warning("Important message.")
    >>> log_manager.critical("Critical Issue occurred.")


The module contains the following methods:

- `__init__(log_file, log_level, log_name)` - creates the instance of the class.
- `info(msg)` - logs the informational message.
- `error(msg)` - logs the error message.
- `warning(msg)` - logs the warning message.
- `debug(msg)` - logs the debug message.
- `critical(msg)` - logs the critical message.
"""

import logging


class LogManager:
    def __init__(self, log_file: str = './Custom-Python_Tools.log', log_level: int = logging.DEBUG, log_name: str = 'LogManager') -> None:
        """
        Initialize the LogManager class.

        Args:
            log_file: The name of the log file.
            log_level: The logging level.
            log_name: The logging name.
        """
        self.log_file = log_file
        self.log_level = log_level
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message: str) -> None:
        """Log a message with severity 'INFO'.

        Args:
            message: The message to log.

        Returns:
            None
        """
        self.logger.info(message)

    def debug(self, message: str) -> None:
        """Log a message with severity 'DEBUG'.

        Args:
            message (str): The message to log.

        Returns:
            None
        """
        self.logger.debug(message)

    def warning(self, message: str) -> None:
        """Log a message with severity 'WARNING'.

        Args:
            message (str): The message to log.

        Returns:
            None
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log a message with severity 'ERROR'.

        Args:
            message (str): The message to log.

        Returns:
            None
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a message with severity 'CRITICAL'.

        Args:
            message (str): The message to log.

        Returns:
            None
        """
        self.logger.critical(message)
