# Function to check and print current system usage (CPU and/or RAM)
def check_system_usage(resource):
    if resource == 'cpu':
        print("CPU Usage:", get_cpu_usage(), "%")
    elif resource == 'ram':
        print("RAM Usage:", get_ram_usage(), "%")
    else:
        print("Invalid input")

