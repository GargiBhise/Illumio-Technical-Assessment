# Illumio-Technical-Assessment

# Log Parser

## Description
This Python script (`app.py`) processes log files and uses a lookup table to categorize log entries by their port and protocol, then outputs the counts of each tag and port-protocol pair. It supports a specific log format and version 2 of the input files.

## Features
- Parses logs to extract port numbers.
- Maps ports to protocol tags using a lookup table (`lookup_table`).
- Counts occurrences of each tag and port-protocol combination.
- Outputs results to CSV files (`port_protocol_counts`, `tags_counts`).

## Assumptions
- The log file follows a specific format (the sixth space-separated field contains the port number).
- The lookup table file is provided in the repository with the format `Port,Protocol,Tag`.
- Only version 2 of the lookup table is supported.
- Unknown ports are assigned the protocol "Unknown" and the tag "Untagged".

## Files in the Repository
- `app.py`: The main Python script that processes logs.
- `lookup_table`: A predefined lookup table used to map port numbers to protocol tags.
- `logs.log`: The log file to be processed by the script.
- `port_protocol_counts`: The output file containing port and protocol counts.
- `tags_counts`: The output file containing tag counts.

## Instructions to Clone or Download

### Option 1: Clone the Repository and Run the Program
1. Open a terminal or command prompt.
2. Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/GargiBhise/Illumio-Technical-Assessment.git
3. Navigate into the repository directory
   cd Illumio-Technical-Assessment
4. Execute the app.py script. It will process the logs in the logs.log file and generate the output files.
   python3 app.py

## After running the script, two output files will be generated:

tags_counts: Contains the counts of each tag.
port_protocol_counts: Contains the counts of each port-protocol combination.

## Tests Performed
The script has been tested with various log formats and lookup tables to ensure proper functionality.
Verified that logs with unknown ports are categorized as "Unknown" with the tag "Untagged".
