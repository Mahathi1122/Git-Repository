import logging
import os
from datetime import datetime

# Create log file name based on current time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Print the log file path for debugging
print(f"Log file will be created at: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

if __name__ == "__main__":
    logging.info("Logging has started")
