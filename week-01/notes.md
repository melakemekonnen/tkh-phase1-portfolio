# 🗺️ Linux Security Labs — Portfolio

> A collection of hands-on Linux security labs completed as part of a cybersecurity fundamentals course.
> All labs were performed by **SSH-ing from a Mac into a Linux VM using VS Code** (Remote - SSH extension).

---

## 📚 Table of Contents

- [Session 01 — Linux Scavenger Hunt](#session-01--linux-scavenger-hunt)
- [Session 02 — Linux Permissions & Hardening](#session-02--linux-permissions--hardening)
- [Session 03 — Stream Editing & Automation](#session-03--stream-editing--automation)
- [TLAB-01 — Operation Clean Sweep](#tlab-01--operation-clean-sweep)

---

## 🗺️ Session 01 — Linux Scavenger Hunt

### Overview
A hands-on lab focused on mapping the Filesystem Hierarchy Standard (FHS), navigating system directories, and extracting hidden system intelligence using core terminal commands.

### 🎯 Objectives
- Navigate the Linux filesystem using absolute and relative paths
- Explore restricted and hidden directories
- Extract system artifacts and document findings
- Push a discovery report to a GitHub portfolio

### 📁 Findings
Navigated to `/var/log`, `/opt/alpha`, and `/var/tmp/.blackout` to verify system logs, extract a mission message, and retrieve a hidden digital token.

### 📄 Artifact
Findings documented in `artifact/discovery.txt`.

---

## 🛡️ Session 02 — Linux Permissions & Hardening

### Overview
A hands-on lab focused on diagnosing and fixing Linux permission misconfigurations using core security commands — `chmod`, `chown`, and `ls`.

### 🎯 Objectives
- Audit file and directory permissions
- Repair restricted access using `chmod`
- Restore secure ownership using `chown`
- Automate remediation using a hardening script

### 📁 Findings
Identified and remediated permission misconfigurations across three targets — a locked vault directory, an unreadable secrets file, and a critically over-permissioned `/etc/shadow` file.

### 📄 Artifact
All findings documented in`artifact/harden.sh`.

---

## ⚙️ Session 03 — Stream Editing & Automation

### Overview
A hands-on lab focused on stream editing and automation using `grep`, `sed`, and `awk`. The exercises demonstrated filtering, parsing, and processing system and web server logs to detect failed login attempts and malicious activity.

### 🎯 Objectives
- Filter logs to find relevant events using `grep`
- Extract and format data using `awk`
- Remove duplicates and clean data using `sort | uniq`
- Save all findings as a separate artifact for security analysis

### 📁 Findings
Parsed `auth.log` to count failed login attempts and analyzed `access.log` to extract unique attacker IPs from SQL injection attempts using `grep`, `awk`, and `sort | uniq`.

### 📄 Artifact
All findings documented in `artifact/threat_ips.txt`.

---

## 🔴 TLAB-01 — Operation Clean Sweep

### Overview
A synthesized threat lab combining navigation, permissions, and stream editing skills to simulate a real incident response scenario. A compromised server was left with a sabotaged log file and broken directory structure — the objective was to navigate the environment, restore access, and extract forensic evidence.

### 🎯 Objectives
- Locate hidden evidence in a non-standard directory
- Repair broken permissions to restore file access
- Parse and clean a 5,000 line log file to extract attacker IPs
- Produce a final threat report as a forensic artifact

### 📁 Findings
Located a hidden `.evidence_cache` directory in `/var/tmp/` with permissions set to `000`. Restored read access to `raw_incident.log`, filtered `CRITICAL` log entries, stripped malware user-agent strings using `sed`, and extracted a deduplicated list of unique attacker IPs using `awk` and `sort | uniq`.

### 📄 Artifact
All findings documented in `artifact/final_threat_report.txt`.

---

*Completed as part of a Linux fundamentals & cybersecurity course.*