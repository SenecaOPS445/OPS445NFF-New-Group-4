#!/usr/bin/env python3
import os
import argparse

"""
This Python script allows you to check the current CPU and/or RAM usage of your Linux system. 

Run the script with the following commands:
- `python3 assignment2.py cpu` to check CPU usage.
- `python3 assignment2.py ram` to check RAM usage.
- `python3 assignment2.py ram cpu` to check RAM and CPU usage.
- `python3 assignment2.py` (without arguments) to check both CPU and RAM usage.

This script reads data from `/proc/stat` for CPU usage and `/proc/meminfo` for memory usage, so it works only on Linux. 
The CPU and RAM usage are displayed as percentages (e.g., `CPU Usage: 45.67 %` and `RAM Usage: 75.34 %`).
"""

# Function to get CPU usage percentage from /proc/stat
def get_cpu_usage():
    f = open('/proc/stat', 'r')
    line = f.readline()
    f.close()

    # Extract the CPU times from the first line
    cpu_data = line.split()[1:8]  # Skip the 'cpu' part and get the time values

    # Convert each value to an integer
    user_time = int(cpu_data[0])
    nice_time = int(cpu_data[1])
    system_time = int(cpu_data[2])
    idle_time = int(cpu_data[3])
    iowait_time = int(cpu_data[4])
    irq_time = int(cpu_data[5])
    softirq_time = int(cpu_data[6])

    total_time = user_time + nice_time + system_time + idle_time + iowait_time + irq_time + softirq_time
    idle_time_total = idle_time + iowait_time
    cpu_usage = (1 - (idle_time_total / total_time)) * 100  # Calculate CPU usage percentage
    return round(cpu_usage, 2)  # Round to 2 decimal places


# Function to get RAM usage percentage from /proc/meminfo
def get_ram_usage():
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()


    total_memory = int(lines[0].split()[1])  
    free_memory = int(lines[1].split()[1])   
    buffers = int(lines[3].split()[1])       
    cached = int(lines[4].split()[1])        

# Function to check and print current system usage (CPU and/or RAM)
def check_system_usage(resources):
    if len(resources) == 0:  # If no resources are provided
        cpu_usage = get_cpu_usage()
        ram_usage = get_ram_usage()
        print("CPU Usage:", cpu_usage, "%")
        print("RAM Usage:", ram_usage, "%")
    elif resources == ['cpu']:  # If only 'cpu' is specified
        cpu_usage = get_cpu_usage()
        print("CPU Usage:", cpu_usage, "%")
    elif resources == ['ram']:  # If only 'ram' is specified
        ram_usage = get_ram_usage()
        print("RAM Usage:", ram_usage, "%")
    else:
        # Handle invalid input
        print("Error: Invalid resource specified. Please specify 'cpu' or 'ram'.")

# Main function with argparse to handle command line arguments
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()
    # Define the argument for resource (cpu or ram)
    parser.add_argument('resource', help="Specify 'cpu' for CPU usage or 'ram' for RAM usage.", type=str, default=None,)
    # Parse the arguments from the command line
    args = parser.parse_args()
    # Call the function based on the provided argument
    check_system_usage(args.resource)
