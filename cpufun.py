#!/usr/bin/env python3
import os
import argparse

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
