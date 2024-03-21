# *LogManager*
`The LogManager class provides a customizable logging utility in Python, allowing you to log messages of different severity levels to both a file and the console.`

## **Features**
- Initialization of logging parameters such as log file name, log level, and log name.
- Logging of messages with severity levels including INFO, DEBUG, WARNING, ERROR, and CRITICAL.
- Configuration of logging to both file and console.
Customizable log message format.

`To use the LogManager class, follow these steps:`

```python
# Import the LogManager class:
from log_manager.log_manager import LogManager

# Create an instance of the LogManager class:
log_manager = LogManager()
```
`By default, this initializes the logger with the following settings:`
- Log file name: './Custom-Python_Tools.log'
- Log level: logging.DEBUG
- Log name: 'LogManager'

`Log messages with desired severity levels:`<br>
Use the appropriate methods to log messages with different severity levels:
- info(message: str)
- debug(message: str)
- warning(message: str)
- error(message: str)
- critical(message: str)

`Example:`
```python
log_manager.info("This is an informational message.")
log_manager.error("An error occurred!")
```

`Customize LogManager settings (optional):`<br>
You can customize the LogManager settings by providing parameters during initialization:

```python
log_manager = LogManager(log_file='my_log.log', log_level=logging.INFO, log_name='MyLogger')
```

 `Logging Format`

The default logging format includes the following fields:

- Timestamp (%(asctime)s)
- Logger Name (%(name)s)
- Log Level (%(levelname)s)
- Log Message (%(message)s)

You can modify the logging format by updating the formatter string in the __init__ method of the LogManager class.