import re

# Regular expression to capture lines with 'WARNING' or 'ERROR'
pattern = r"(WARNING|ERROR)"

# Path to the log file
log_file_path = "/var/log/syslog"

#open and read the log file Opening and Reading the Log File
#Opens the file in read mode ("r").The with statement ensures that the file is properly closed after reading.
with open (log_file_path, "r") as file: 
    for line in file:  #Reads the file line by line, processing one line at a time.
        if re.search(pattern,line): #re.search(pattern, line): Checks if the line contains either "WARNING" or "ERROR".If the pattern is found, the condition evaluates to True.
            print(line.strip()) #line.strip() removes leading and trailing spaces or newline characters. Prints the line only if it contains "WARNING" or "ERROR".


