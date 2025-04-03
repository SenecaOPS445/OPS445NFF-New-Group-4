def get_ram_usage():
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()

    # To extract the total ram and free memory values 
    total_memory = int(lines[0].split()[1])   
    free_memory = int(lines[1].split()[1])   
    buffers = int(lines[3].split()[1])
    cached = int(lines[4].split()[1])




