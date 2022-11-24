import logging
from termcolor import colored

"""Audit & Log"""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

logger.info(colored("User X ran the /start command.", "green", attrs=["blink"]))


