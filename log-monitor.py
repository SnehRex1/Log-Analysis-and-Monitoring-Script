import time
import signal
import logging
import random

# Configure logging
logging.basicConfig(filename='log_monitor.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

def signal_handler(sig, frame):
    logger.info("Logging interrupted. Exiting.")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:
            file.seek(0, 2)  # Move the cursor to the end of the file
            while True:
                line = file.readline()
                if line:
                    logger.info("New log entry: %s", line.strip())
                time.sleep(0.1)
    except FileNotFoundError:
        logger.error("Log file not found.")
        exit(1)

def analyze_log(log_file):
    try:
        with open(log_file, 'r') as file:
            log_data = file.readlines()
            keywords = ['ERROR', 'HTTP']  # Add more keywords as needed
            keyword_counts = {keyword: 0 for keyword in keywords}
            for line in log_data:
                for keyword in keywords:
                    if keyword in line:
                        keyword_counts[keyword] += 1
            logger.info("Keyword counts:")
            for keyword, count in keyword_counts.items():
                logger.info("%s: %d", keyword, count)
    except FileNotFoundError:
        logger.error("Log file not found.")
        exit(1)

def main():
    log_file = 'example.log'  # Change this to your log file path

    # Monitor log file
    logger.info("Starting log monitoring...")
    monitor_log(log_file)

    # Analyze log file
    logger.info("Starting log analysis...")
    analyze_log(log_file)

    # Continuously log messages at different levels
    logger.info("Starting continuous logging...")
    while True:
        try:
            log_level = random.choice(log_levels)
            log_message = formats[log_level]
            logger.log(log_level, log_message)
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Logging interrupted. Exiting.")
            break

if __name__ == "__main__":
    main()