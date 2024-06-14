# logging_config.py

import logging

LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILE = 'gradebotguru.log'

def setup_logging(level=LOGGING_LEVEL, format=LOGGING_FORMAT, filename=LOGGING_FILE):
    # Clear existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(
        level=level,
        format=format,
        filename=filename,
        filemode='a'  # Append mode
    )
    
    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(logging.Formatter(format))
    logging.getLogger('').addHandler(console)
