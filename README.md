# Log-Analysis-and-Monitoring-Script
# Log Monitor and Analyzer

This Python script monitors a specified log file for new entries and performs basic analysis on the log entries, such as counting occurrences of specific keywords. It also logs messages at different levels (INFO, DEBUG, ERROR) in a continuous loop.

## Prerequisites

- Python 
- Access to a log file that you want to monitor and analyze

## Dependencies

- Python's built-in modules: `time`, `signal`, `logging`, `random`

## Testing

You can test the script by creating a sample log file and adding entries to it while the script is running. You should see the new entries being logged in `log_monitor.log`.

## Features

- Monitors a specified log file for new entries in real-time
- Performs basic analysis on log entries, such as counting occurrences of specific keywords
- Handles errors and logs feedback on script execution
- Logs messages at different levels (INFO, DEBUG, ERROR) in a continuous loop

## Code Explanation 

The script starts by setting up a logging configuration using logging.basicConfig. This specifies the filename, log level, and format of the log messages.

The signal_handler function is defined to handle the SIGINT signal (typically generated by the user pressing Ctrl+C). When this signal is received, it logs a message and exits the program.

The monitor_log function opens a log file and continuously reads new entries from the end of the file. If a new line is found, it logs the new entry. If the file is not found, it logs an error and exits the program.

The analyze_log function opens a log file and reads all the lines. It counts the occurrences of specific keywords (‘ERROR’, ‘HTTP’) in the lines and logs the counts. If the file is not found, it logs an error and exits the program.

The main function specifies the log file path, starts the log monitoring, and then starts the log analysis. It also starts a continuous loop that logs messages at different levels (INFO, DEBUG, ERROR).

The script is run from the command line with python log-monitor.py.
