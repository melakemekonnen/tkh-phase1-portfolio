#!/usr/bin/env python3
import subprocess
import json

print("[*] Initiating Automated Threat Hunt...")

# TASK 1: Use subprocess to grep for "Failed password" in the log file
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# TASK 2: Parse the output and extract attacking IP addresses
lines = raw_output.split('\n')

attacker_ips = []

for line in lines:
    if line:
        ip = line.split(" ")[10]
        attacker_ips.append(ip)

# TASK 3: Create dictionary and export to JSON
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": attacker_ips
}

with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print(f"[*] {len(attacker_ips)} attacker IPs extracted to threat_report.json")
print("[+] Threat Hunt Complete. Report generated.")
