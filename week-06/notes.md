# 🏰 Titan Hardened Outpost — Security Operations Portfolio

> A capstone security engineering project completed as part of The Forge — a 6-week cybersecurity fundamentals sprint.
> All labs were performed by **SSH-ing from a local machine into an Ubuntu Linux VM using VS Code** (Remote - SSH extension).

---

## 📚 Table of Contents

- [Session 16 — The Architect's War Room](#session-16--the-architects-war-room)
- [Session 17 — The Forge Final](#session-17--the-forge-final)
- [Session 18 — The Hardened Outpost](#session-18--the-hardened-outpost)

---

## 🔬 Session 16 — The Architect's War Room

### Overview
A break/fix diagnostic lab focused on mapping real system failures to their correct OSI layers and restoring a deliberately sabotaged environment to operational status using the Outside-In troubleshooting methodology.

### 🎯 Objectives
- Diagnose and repair a file permission lockout using `chmod`
- Identify and evict a ghost Docker container squatting on a production port
- Locate and delete a UFW firewall rule blocking outbound ICMP traffic
- Map each failure to its correct OSI layer (Layer 3, 4, and 7)

### 📁 Findings
- **Anomaly 1 (Layer 7):** `broken_script.sh` had `----------` permissions. Fixed with `chmod 755`.
- **Anomaly 2 (Layer 4):** `ghost_web` container was occupying port 8080. Removed with `docker rm -f ghost_web`.
- **Anomaly 3 (Layer 3):** UFW had a `DENY OUT` rule blocking ICMP. Deleted with `sudo ufw delete [rule number]`.

### 📄 Artifact
Findings documented in `readiness_check.log`.

---

## 🏹 Session 17 — The Forge Final

### Overview
A timed technical diagnostic covering both theoretical and practical cybersecurity skills across all five domains — Linux, Networking, Python, Docker, and Active Directory — with no guide and no AI assistance.

### 🎯 Objectives
- Complete a timed theory quiz covering OSI layers, subnetting, AD hierarchy, and Python logic
- Use `find` to locate hidden root-owned `.log` files across the entire filesystem
- Extract and secure the files using `sudo mv` and `chmod 444`
- Document all commands in a formal exam report

### 📁 Findings
- Located `forge_alpha.log` at `/tmp/audit_internal/` and `forge_beta.log` at `/var/opt/system_logs/` using:
```bash
  find / -user root -name "*.log" 2>/dev/null
```
- Moved both files into `~/Exam_Submission/` and locked them to read-only (`r--r--r--`) with `chmod 444`.

### 📄 Artifact
All findings documented in `practical_exam_report.txt`.

---

## 🏰 Session 18 — The Hardened Outpost (Capstone)

### Overview
A solo 3-hour capstone deployment of a fully integrated, hardened enterprise environment for the fictional client Titan Small Business Services. Covered SSH hardening, firewall configuration, Python automation, and Docker network segmentation.

### 🎯 Objectives
- Harden SSH by disabling root login and password authentication
- Configure UFW with a default-deny policy and explicit allow rules
- Write a Python auditing script to monitor disk usage and write telemetry to a log file
- Deploy an air-gapped Docker Compose stack with frontend/backend network isolation
- Compile all work into a professional Security Architecture Document (SAD)

### 📁 Findings
- **SSH Hardening:** Disabled `PermitRootLogin` and `PasswordAuthentication` in `/etc/ssh/sshd_config`.
- **Firewall:** Default deny incoming, explicit allow on ports 22 (SSH) and 8080 (web app).
- **Python Auditor:** `sys_auditor.py` runs `df -h` and writes output to `/var/log/sys_audit.log`.
- **Docker Stack:** `wiki` (nginx) exposed on port 8080 via `frontend` network. `db` (mysql) isolated on `backend` network with `internal: true` — completely unreachable from the host.

### 📄 Artifact
Full deployment documented in `HardenedOutpost_SAD.pdf`.

---

## 🧠 Skills Demonstrated

| Domain | Tools & Concepts |
|---|---|
| Linux Hardening | `chmod`, `chown`, `sshd_config`, UFW |
| Network Diagnostics | OSI Layers 3/4/7, `ping`, `nc`, `ss`, `ufw` |
| Docker | Containers, Docker Compose, network isolation, port management |
| Python | `os` module, file I/O, system automation |
| Forensics | `find`, `mv`, file permissions, log analysis |

---

## References
Forouzan, B. (2007). *Data communications and networking* (4th ed.).
McGraw-Hill.

NIST. (2020). *Security and privacy controls for information systems
and organizations* (SP 800-53 Rev. 5). National Institute of
Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5

Tanenbaum, A., & Wetherall, D. (2011). *Computer networks* (5th ed.).
Prentice Hall.

*Completed as part of The Forge — Sprint 1 Capstone | Junior Security Operator Certification.*
