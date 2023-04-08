import platform
import psutil

import subprocess

# get the operating system details
os_name = platform.system()
os_release = platform.release()
os_version = platform.version()

# get the CPU details
cpu_name = platform.processor()
cpu_cores = psutil.cpu_count(logical=True)

# get the memory details
mem = psutil.virtual_memory()
mem_total = mem.total // (1024 ** 3)
mem_available = mem.available // (1024 ** 3)

# get the disk details
disk = psutil.disk_usage('/')
disk_total = disk.total // (1024 ** 3)
disk_used = disk.used // (1024 ** 3)
disk_free = disk.free // (1024 ** 3)

# print the computer details
print(f"Operating System: {os_name} {os_release} ({os_version})")
print(f"CPU: {cpu_name} ({cpu_cores} cores)")
print(f"Memory: {mem_total}GB (Available: {mem_available}GB)")
print(f"Disk: {disk_total}GB (Used: {disk_used}GB, Free: {disk_free}GB)")


# Run the wmic command to get the list of installed software and their versions
command = "wmic product get name, version"
output = subprocess.check_output(command, shell=True, universal_newlines=True)

# Split the output into lines and skip the first two lines (header)
lines = output.strip().split('\n')[2:]

# Extract the software names and versions and print them
software_info = [line.strip().rsplit('  ', 1) for line in lines]
for info in software_info:
    if len(info) >= 2:
        name, version = info
        print(f"{name} - {version}")

with open("software_list.txt", "w") as f:
    software_info = [line.strip().rsplit('  ', 1) for line in lines]
    for info in software_info:
        if len(info) >= 2:
            name, version = info
            f.write(f"{name} - {version}\n")