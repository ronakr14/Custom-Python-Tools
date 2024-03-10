import logging


class LogManager:
    def __init__(self, log_file: str = 'Custom-Python_Tools.log', log_level: int = logging.DEBUG, log_name: str = 'LogManager'):
        """
        Initialize the LogManager class.

        Args:
            log_file (str, optional): The name of the log file. Defaults to 'Custom-Python_Tools.log'.
            log_level (int, optional): The logging level. Defaults to logging.DEBUG.
        """
        self.log_file = log_file
        self.log_level = log_level
        self.logger = logging.getLogger(log_name)
        print("*****************")
        print(self.logger)
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

    def info(self, message: str):
        """
        Log a message with severity 'INFO'.

        Args:
            message (str): The message to log.

        Returns:
            None

        """
        self.logger.info(message)

    def debug(self, message: str):
        """
        Log a message with severity 'DEBUG'.

        Args:
            message (str): The message to log.

        Returns:
            None

        """
        self.logger.debug(message)

    def warning(self, message: str):
        """
        Log a message with severity 'WARNING'.

        Args:
            message (str): The message to log.

        Returns:
            None

        """
        self.logger.warning(message)

    def error(self, message: str):
        """
        Log a message with severity 'ERROR'.

        Args:
            message (str): The message to log.

        Returns:
            None

        """
        self.logger.error(message)

    def critical(self, message: str):
        """
        Log a message with severity 'CRITICAL'.

        Args:
            message (str): The message to log.

        Returns:
            None

        """
        self.logger.critical(message)
