import os
import time
import datetime

# Configure process name and log file path
# process_name = "VLC"  # Replace with the name of your process
# log_file = "process_usage_log_VLC.csv"
base = "/Users/danielarturi/Desktop/McGill Fall 2024/ECSE 429/Project/PartC/ECSE429_PartC/"
log_file = base + "intermediate_findings/dynamicAnalysisLog/raw_log_data14.csv"

page_size = 16384


def get_process_usage():
    """
    Fetch memory and CPU usage for a specific process.
    """
    try:
        # Run a shell command to fetch process information
        result_cpu = os.popen(f"top -l 1 | grep -E 'CPU'").read().strip()
        result_mem = os.popen(f"vm_stat").read().strip()

        # Extract values if the process is running
        if result_cpu and result_mem:
            lines_cpu = result_cpu.split('\n')
            lines_mem = result_mem.split('\n')
            usage_data = []

            cpu_info = lines_cpu[0].split(" ");
            usage_data.append({
                "user cpu usage": float(cpu_info[2][:-1]),
                "system cpu usage": float(cpu_info[4][:-1]),
                "idle cpu percentage": float(cpu_info[6][:-1]),
                "bytes available": int(lines_mem[1].split(" ")[-1][:-1]) * page_size,
                "bytes active": int(lines_mem[2].split(" ")[-1][:-1]) * page_size,
            })
            return usage_data
        else:
            return None
    except Exception as e:
        print(f"Error fetching process usage: {e}")
        return None


def log_usage():
    """
    Log memory and CPU usage to a file.
    """
    with open(log_file, "w") as f:
        header = "time, user cpu usage, system cpu usage, idle cpu percentage, bytes available, bytes active\n"
        f.write(header)
        while True:
            usage_data = get_process_usage()
            if usage_data:
                for data in usage_data:
                    log_entry = (f"{datetime.datetime.now()} , "
                                 f"{data['user cpu usage']}%, {data['system cpu usage']}%, {data['idle cpu percentage']}%, "
                                 f"{data['bytes available']}, {data['bytes active']}\n")
                    f.write(log_entry)
                    # print(log_entry.strip())
            else:
                f.write(f"{datetime.datetime.now()} | Process not found\n")
                print(f"{datetime.datetime.now()} | Process not found")
            time.sleep(0.1)  # Log every second


if __name__ == "__main__":
    print(f"Logging cpu and memory usage to '{log_file}'...")
    log_usage()
