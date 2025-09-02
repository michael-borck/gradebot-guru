import logging

from pytest_mock import MockerFixture

from gradebotguru.logging_config import setup_logging


def test_setup_logging_default(mocker: MockerFixture) -> None:
    """
    Test default logging configuration.

    Ensures that the default logging configuration is correctly set up with
    both file and console handlers at the INFO level.
    """
    setup_logging()
    logger = logging.getLogger("")
    assert logger.level == logging.INFO
    assert any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)
    assert any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers
    )


def test_setup_logging_custom_file(mocker: MockerFixture) -> None:
    """
    Test custom logging file configuration.

    Ensures that the logging configuration correctly uses a custom log file.
    """
    mocker.patch("gradebotguru.logging_config.LOGGING_FILE", "test.log")
    setup_logging(filename="custom.log")
    logger = logging.getLogger("")
    assert any(
        handler.baseFilename.endswith("custom.log")
        for handler in logger.handlers
        if isinstance(handler, logging.FileHandler)
    )


def test_setup_logging_custom_level(mocker: MockerFixture) -> None:
    """
    Test custom logging level configuration.

    Ensures that the logging configuration correctly sets the logging level to DEBUG.
    """
    setup_logging(level=logging.DEBUG)
    logger = logging.getLogger("")
    assert logger.level == logging.DEBUG


def test_setup_logging_custom_format(mocker: MockerFixture) -> None:
    """
    Test custom logging format configuration.

    Ensures that the logging configuration correctly uses a custom log format.
    """
    custom_format = "%(levelname)s: %(message)s"
    setup_logging(format=custom_format)
    logger = logging.getLogger("")
    assert any(handler.formatter._fmt == custom_format for handler in logger.handlers)
