# monitor.py

import psutil
import time
from datetime import datetime

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def print_system_stats():
    while True:
        print(f"Data e Hora: {datetime.now()}")
        print(f"Uso da CPU: {get_cpu_usage()}%")
        print(f"Uso da Memória: {get_memory_usage()}%")
        print(f"Uso do Disco: {get_disk_usage()}%")
        print("-" * 30)
        time.sleep(5)

if __name__ == "__main__":
    print_system_stats()
