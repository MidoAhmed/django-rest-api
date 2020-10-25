"""
Keys and secrets should be loaded of the environment.
Put here only things that are shared between all production deployments.
"""
from .base import *

# Get an instance of a logger
logger = logging.getLogger(__name__)

logger.debug(" Settings loading: %s" % __file__)
