"""
These should mimic a production settings making minimal modifications to accommodate tests
"""

import environ
from pathlib import Path


print("Settings loading: %s" % __file__)

# This will read missing environment variables from a file
# We want to do this before loading any base settings as they may depend on environment
environ.Env.read_env(str(Path(__file__).parent / ".test.env"), DEBUG='False')

# noinspection PyUnresolvedReferences
from .base import *
