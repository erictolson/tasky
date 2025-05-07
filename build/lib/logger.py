import logging

# Configure logger
logger = logging.getLogger("tasky")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("tasky.log")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler if not already added
if not logger.hasHandlers():
    logger.addHandler(file_handler)
