#!/usr/bin/env python3
import os
import argparse

"""
This Python script allows you to check the current CPU and/or RAM usage of your Linux system. 

Run the script with the following commands:
- `python3 assignment2.py cpu` to check CPU usage.
- `python3 assignment2.py  ram` to check RAM usage.
- `python3 assignment2.py  (without arguments) to check both CPU and RAM usage.

This script reads data from `/proc/stat` for CPU usage and `/proc/meminfo` for memory usage, so it works only on Linux. 
The CPU and RAM usage are displayed as percentages (e.g., `CPU Usage: 45.67 %` and `RAM Usage: 75.34 %`).
"""


def get_cpu_usage():
    f = open('/proc/stat', 'r')
    line = f.readline()
    f.close()

    
    cpu_data = line.split()[1:8]  

    
    user_time = int(cpu_data[0])
    nice_time = int(cpu_data[1])
    system_time = int(cpu_data[2])
    idle_time = int(cpu_data[3])
    iowait_time = int(cpu_data[4])
    irq_time = int(cpu_data[5])
    softirq_time = int(cpu_data[6])

    total_time = user_time + nice_time + system_time + idle_time + iowait_time + irq_time + softirq_time
    idle_time_total = idle_time + iowait_time
    cpu_usage = (1 - (idle_time_total / total_time)) * 100  
    return round(cpu_usage, 2)  
