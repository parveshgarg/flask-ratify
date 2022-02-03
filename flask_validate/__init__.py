# -*- coding: utf-8 -*-
"""
    flask_validate
    ~~~~
    flask-validate is a simple extension to Flask allowing you to validate requests
    using jsonschema

    jsonschema is supported for headers, params, and body (json only)

    For schema details used in flask-validate, see docs/schema.md
    For jsonschema details, check https://pypi.org/project/jsonschema/ and https://json-schema.org/understanding-json-schema/

    :copyright: (c) 2022 by Parvesh Garg.
    :license: Apache Software License 2.0, see LICENSE for more details.
"""

from .version import __version__
from .decorator import validate
from .extension import FlaskValidate


import logging
from logging import NullHandler


__all__ = ['validate', 'FlaskValidate']

rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())

if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
