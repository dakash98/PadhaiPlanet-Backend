"""
This module configures the logger. It should be imported before initializing flask app in app.py,
so that these configuration can be applied to flasks' inbuilt logger.
"""

import logging
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        'disable_existing_loggers': False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] - [%(levelname)s] - [%(filename)s] - [%(funcName)s()] %(message)s",
            }
        },
        "handlers": {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "service.log",
                "maxBytes": 1000000,
                "backupCount": 10,
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ['wsgi', 'file']},
    }
)

logger = logging.getLogger()
