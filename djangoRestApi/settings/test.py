"""
These should mimic a production settings making minimal modifications to accommodate tests
"""
from .base import *

# Get an instance of a logger
logger = logging.getLogger(__name__)

logger.debug(" Settings loading: %s" % __file__)
