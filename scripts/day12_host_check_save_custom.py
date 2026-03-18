import os

hosts = ["8.8.8.8", "1.1.1.1", "google.com"]

report_file = "custom_host_report.txt"

with open(report_file, "w", encoding="utf-8") as file:
    for host in hosts:
        result = os.system(f"ping -n 1 {host}")

        if result == 0:
            status = "reachable"
        else:
            status = "not reachable"

        line = f"{host}: {status}\n"
        file.write(line)
        print(line.strip())

print("Custom report created")