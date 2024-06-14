# ADR 0002: Logging Configuration

## Status

Accepted

## Context

GradeBot Guru needs a robust and flexible logging system to help with debugging and monitoring. The logging system should support different logging levels, formats, and handlers (e.g., console and file handlers). This ensures that developers can easily trace the application's behavior and capture important events.

## Decision

We will implement the logging configuration in `logging_config.py` that:
1. Defines the default logging settings (level, format, handlers).
2. Provides a `setup_logging` function to configure the logging system based on these settings.
3. Allows for customization of logging settings via parameters to the `setup_logging` function.

### Implementation

1. **Define Logging Settings:**

   We define the default logging settings, including log levels, log formats, and handlers.

   ```python
   # logging_config.py

   import logging

   LOGGING_LEVEL = logging.INFO
   LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   LOGGING_FILE = 'gradebotguru.log'
   ```

2. **Implement the `setup_logging` Function:**

   The `setup_logging` function configures the logging system based on the defined settings and any overrides provided.

   ```python
   # logging_config.py

   import logging

   LOGGING_LEVEL = logging.INFO
   LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   LOGGING_FILE = 'gradebotguru.log'

   def setup_logging(level=LOGGING_LEVEL, format=LOGGING_FORMAT, filename=LOGGING_FILE):
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
   ```

3. **Write Unit Tests for the Logging Configuration:**

   We write unit tests using `pytest` to ensure the logging configuration works correctly.

   ```python
    import logging
    import pytest
    from pytest_mock import MockerFixture
    from gradebotguru.logging_config import setup_logging


    def test_setup_logging_default(mocker: MockerFixture) -> None:
        """
        Test default logging configuration.

        Ensures that the default logging configuration is correctly set up with
        both file and console handlers at the INFO level.
        """
        setup_logging()
        logger = logging.getLogger('')
        assert logger.level == logging.INFO
        assert any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)
        assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)


    def test_setup_logging_custom_file(mocker: MockerFixture) -> None:
        """
        Test custom logging file configuration.

        Ensures that the logging configuration correctly uses a custom log file.
        """
        mocker.patch('gradebotguru.logging_config.LOGGING_FILE', 'test.log')
        setup_logging(filename='custom.log')
        logger = logging.getLogger('')
        assert any(handler.baseFilename.endswith('custom.log') for handler in logger.handlers if isinstance(handler, logging.FileHandler))


    def test_setup_logging_custom_level(mocker: MockerFixture) -> None:
        """
        Test custom logging level configuration.

        Ensures that the logging configuration correctly sets the logging level to DEBUG.
        """
        setup_logging(level=logging.DEBUG)
        logger = logging.getLogger('')
        assert logger.level == logging.DEBUG


    def test_setup_logging_custom_format(mocker: MockerFixture) -> None:
        """
        Test custom logging format configuration.

        Ensures that the logging configuration correctly uses a custom log format.
        """
        custom_format = '%(levelname)s: %(message)s'
        setup_logging(format=custom_format)
        logger = logging.getLogger('')
        assert any(handler.formatter._fmt == custom_format for handler in logger.handlers)
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The logging configuration can be customized to different levels, formats, and handlers as needed.
- **Robustness:** By providing both file and console handlers, we ensure that logs are captured persistently and are visible in real-time.
- **Testability:** Unit tests can verify that the logging configuration is set up correctly under various conditions.

### Negative Consequences

- **Complexity:** Introducing customizable logging settings adds some complexity to the configuration process.
- **Maintenance:** Ensuring that all logging settings are properly managed and updated requires ongoing maintenance.

## Alternatives Considered

1. **Hardcoding Logging Settings:**
   - This approach would have been simpler but far less flexible and scalable.

2. **Using a Single Logging Handler:**
   - Relying solely on a console or file handler would limit the visibility and persistence of logs.

## Conclusion

The chosen approach of implementing a flexible logging configuration in `logging_config.py` provides the necessary flexibility, robustness, and testability for GradeBot Guru. This decision ensures that the application can be easily monitored and debugged, with logs available both in real-time and as persistent records.
