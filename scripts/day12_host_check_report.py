import os
from datetime import datetime

hosts = ["8.8.8.8", "1.1.1.1", "google.com", "github.com", "example.invalid"]

report_name = "host_report.txt"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(report_name, "w", encoding="utf-8") as report:
    report.write("Host Availability Report\n")
    report.write(f"Created: {current_time}\n")
    report.write("=" * 40 + "\n")

    for host in hosts:
        print("Checking:", host)
        result = os.system(f"ping -n 1 {host}")

        if result == 0:
            line = f"{host} - reachable\n"
        else:
            line = f"{host} - not reachable\n"

        print(line.strip())
        report.write(line)

    report.write("=" * 40 + "\n")
    report.write("End of report\n")

print(f"Report saved to {report_name}")