# Week 3 — Python for Security Professionals
**Focus:** Security scripting, system interrogation, network automation
**Sessions:** S7, S8, S9
**Dates:** March 23–27, 2026

---

## Session Summaries

### S7 — Security Scripting & Service Enumeration
This session introduced Python scripting for security purposes, focusing
on automating port scanning and service enumeration tasks that analysts
typically perform manually. The artifact port_check.py automates SSH
port availability checks across multiple target servers, demonstrating
how Python's socket library can replace manual nmap scans for quick
triage tasks (Seitz, 2021).

### S8 — System Interrogation with Python
This session covered using Python to interrogate live systems —
collecting running processes, open files, network connections, and
system metadata programmatically. The artifact system_auditor.py
automates the collection of host-based indicators that a security
analyst would gather during live incident response triage, reducing
human error and response time (Ligh et al., 2014).

### S9 — Network Scripting & TCP Port Connection
This session focused on building TCP client connections and network
scanning tools from scratch using Python's socket library, without
relying on external tools. The artifact brute_detector.py demonstrates
automated detection of brute-force patterns in authentication logs,
combining file I/O with pattern matching — a core capability in custom
SIEM rule development.

---

## Key Concepts
- Python socket library for network communication
- File I/O for log parsing and artifact generation
- Subprocess module for system interrogation
- Automating security workflows with Python scripts

---

## Artifacts
- `port_check.py` — TCP port scanner for SSH availability
- `system_auditor.py` — Host-based system interrogation tool
- `brute_detector.py` — Authentication log brute-force detector
- `incident_response.py` — Automated IR data collection script

---

## References
Ligh, M., Case, A., Levy, J., & Walters, A. (2014). *The art of
memory forensics: Detecting malware and threats in Windows, Linux,
and Mac memory*. Wiley.

Seitz, J. (2021). *Black hat Python: Python programming for hackers
and pentesters* (2nd ed.). No Starch Press.
