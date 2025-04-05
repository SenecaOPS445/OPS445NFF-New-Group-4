# Function to check and print current system usage (CPU and/or RAM)
def check_system_usage(resource):
    if resource == 'cpu':
        cpu_usage = get_cpu_usage()
        print("CPU Usage:", cpu_usage, "%")
    elif resource == 'ram':
        ram_usage = get_ram_usage()
        print("RAM Usage:", ram_usage, "%")
    else:
        print("Error: Invalid resource specified. Please specify 'cpu' or 'ram'.")

