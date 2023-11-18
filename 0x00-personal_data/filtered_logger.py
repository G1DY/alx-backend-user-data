#!/usr/bin/env python3
"""logging module"""
from typing import List
import re
import os
import logging
import mysql.connector
import csv


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """function initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """returns filtered values from log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


PII_FIELDS = ("name", "email", "password", "ssn", "phone")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """takes no arguments and returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(list(PII_FIELDS))
    target_handle.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
