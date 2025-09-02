import logging
import os

LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGING_FILE = "demo/gradebotguru.log"


def setup_logging(
    level: int = LOGGING_LEVEL,
    format: str = LOGGING_FORMAT,
    filename: str | None = LOGGING_FILE,
) -> None:
    """
    Setup logging configuration.

    This function configures the logging settings, including log level, format, and output file.

    Args:
        level (int): Logging level (default is logging.INFO).
        format (str): Logging format string (default is '%(asctime)s - %(name)s - %(levelname)s - %(message)s').
        filename (Optional[str]): Log file name. If None, logs will not be written to a file (default is 'gradebotguru.log').

    Examples:
        >>> import logging
        >>> from io import StringIO
        >>> log_stream = StringIO()
        >>> setup_logging(level=logging.DEBUG, format='%(levelname)s: %(message)s')
        >>> logging.getLogger().handlers = [logging.StreamHandler(log_stream)]
        >>> logger = logging.getLogger()
        >>> logger.debug('This is a debug message')
        >>> log_stream.getvalue().strip()
        'This is a debug message'
        >>> log_stream.close()
    """
    # Clear existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    if filename and os.path.exists(filename):
        # Configure file handler
        logging.basicConfig(
            level=level,
            format=format,
            filename=filename,
            filemode="a",  # Append mode
        )
    else:
        # Configure console handler
        logging.basicConfig(level=level, format=format)
        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(logging.Formatter(format))
        logging.getLogger("").addHandler(console)
