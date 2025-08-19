import logging
import os
from datetime import datetime

# Base directory of project (folder containing src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Logs directory
logs_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode='w'
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    print(f"Logs will be saved to {LOG_FILE_PATH}")
