import os

hosts = ["8.8.8.8", "1.1.1.1", "google.com"]

for host in hosts:
    print("Checking:", host)
    result = os.system(f"ping -n 1 {host}")

    if result == 0:
        print(host, "is reachable")
    else:
        print(host, "is not reachable")

    print("-" * 30)