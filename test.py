import os
import platform
import psutil
import subprocess

# print the computer details
def os_details(): 
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
    details = []
    detail = "Operating System: " + os_name + os_release + os_version
    details.append(detail)
    detail = "CPU: " + str(cpu_name) + str(cpu_cores) + "cores"
    details.append(detail)
    detail = "Memory: " + str(mem_total) + "GB (Available: " + str(mem_available) + "GB)"
    details.append(detail)
    detail = "Disk: " + str(disk_total) + "GB (Used: " + str(disk_used) + "GB, Free: " + str(disk_free) + "GB)"
    details.append(detail)
    return details

# Run the wmic command to get the list of installed software and their versions
def all_files(): 
    allFiles = []
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
            allFiles.append(f"{name} - {version}")
    return allFiles

# def write_txt():
#     with open("software_list.txt", "w") as f:
#         software_info = [line.strip().rsplit('  ', 1) for line in lines]
#         for info in software_info:
#             if len(info) >= 2:
#                 name, version = info
#                 f.write(f"{name} - {version}\n")

def network_config(): 
    print("Hello")
    # Extract network configuration and write to TXT file
    network_config_output = subprocess.check_output('ipconfig /all', shell=True)
    print(network_config_output.decode('utf-8'))
    network_config_output = network_config_output.decode('utf-8')
    return network_config_output




# # Extract network configuration and write to TXT file
# network_config_output = subprocess.check_output('ipconfig /all', shell=True)
# # with open('network_config.txt', 'w') as f:
# #     f.write(network_config_output.decode('utf-8'))

# network_config_output = subprocess.check_output('ipconfig /all', shell=True)
# network_config_output = network_config_output.decode('utf-8')
# print(network_config_output)
# # print(network_config_output.decode('utf-8'))