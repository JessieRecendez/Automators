import os
import psutil
import platform
import subprocess
import psycopg2


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")


def check_memory_usage():
    virtual_memory = psutil.virtual_memory()
    print(f"Memory Usage: {virtual_memory.percent}%")


def check_disk_space():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Disk Usage ({partition.device}): {usage.percent}%")


def check_system_info():
    system_info = platform.uname()
    print(f"System Information: {system_info.system} {system_info.release}")


def check_network_connectivity():
    try:
        subprocess.check_call(["ping", "-c", "1", "google.com"])
        print("Network Connectivity: Online")
    except subprocess.CalledProcessError:
        print("Network Connectivity: Offline")
        

def check_database_connection(host, port, dbname, user, password):
    try:
        conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        print(f"Database Connection: Connected to {host}:{port}/{dbname}")
        conn.close()
    except psycopg2.OperationalError:
        print(f"Database Connection: Unable to connect to {host}:{port}/{dbname}")


if __name__ == "__main__":
    print("System Health Check Report:")
    print("-" * 30)

    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_system_info()
    check_network_connectivity()
    db_host = "localhost"   # change to personal needs.
    db_port = 5432  # change to personal needs.
    db_name = "mydb"    # change to personal needs.
    db_user = "myuser"  # change to personal needs.
    db_password = "mypassword"  # change to personal needs.

    check_database_connection(db_host, db_port, db_name, db_user, db_password)
