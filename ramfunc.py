def get_ram_usage():
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()

    # Extract total and free memory values
    total_memory = int(lines[0].split()[1])  
    free_memory = int(lines[1].split()[1])   
