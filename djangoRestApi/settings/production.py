"""
Keys and secrets should be loaded of the environment.
Put here only things that are shared between all production deployments.
"""

import environ
from pathlib import Path

print("Settings loading: %s" % __file__)

# This will read only MISSING environment variables from a file
# We want to do this before loading any base settings as they may depend on environment
environ.Env.read_env(str(Path(__file__).parent / ".production.env"), DEBUG='False', ASSETS_DEBUG='False')

# noinspection PyUnresolvedReferences
from .base import *
