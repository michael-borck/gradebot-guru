import logging

from pytest_mock import MockerFixture

from gradebotguru.logging_config import setup_logging


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
    assert any(handler.formatter and handler.formatter._fmt == custom_format for handler in logger.handlers)
