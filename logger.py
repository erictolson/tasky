import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="tasky.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log(action, message):
    logging.info(f"{action.upper()}: {message}")
