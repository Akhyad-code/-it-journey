import os

host = input("Enter host or IP: ")

result = os.system(f"ping -n 1 {host}")

if result == 0:
    print(host, "is reachable")
else:
    print(host, "is not reachable")