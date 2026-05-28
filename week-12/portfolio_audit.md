# Portfolio Audit — Phase 1
**Operator:** Melakee Mekonnen
**Date:** May 28, 2026
**GitHub:** https://github.com/melakemekonnen
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Repository Overview

| Repository | Focus | Key Skills Demonstrated |
|---|---|---|
| osint-field-ops | Reconnaissance & OSINT | Host discovery, passive recon, footprinting |
| subnet-recon-ops | Network Mapping | nmap scanning, subnet enumeration, service fingerprinting |
| w8-penetration-testing | Offensive Security | Exploitation, privilege escalation, lateral movement |
| samba-vuln-lab | Vulnerability Exploitation | CVE research, Samba exploitation, service enumeration |
| titan-hardened-outpost | System Hardening | SSH hardening, service minimization, access controls |
| web-app-security-portfolio | Web Application Security | SQL injection, XSS, OWASP Top 10 |
| python-security-automation | Security Tooling | Scripting, automation, custom security tools |
| virtualization-labs | Lab Infrastructure | VM setup, Docker, containerized environments |
| dfir-response-ops | Digital Forensics & IR | Memory forensics, disk imaging, SIEM correlation, chain of custody |
| perimeter-defense-ops | Network Defense | Firewalls, IDS signatures, Suricata, EDR policies, Sysmon |

---

## Phase 1 Skill Summary

### Offensive Skills
- Network reconnaissance using nmap with full-port and service-version scanning
- Credential attacks using Hydra against SSH services
- Command injection exploitation against vulnerable web applications
- Vulnerability identification and exploitation (Samba, Redis, FTP, web shells)

### Defensive Skills
- Live triage on compromised systems without destroying volatile evidence
- Cryptographic chain of custody using MD5 and SHA256
- Memory forensics and deleted file recovery using The Sleuth Kit
- SIEM log correlation and attack timeline reconstruction (ELK/Kibana)
- UFW and iptables firewall engineering including DMZ architecture
- Suricata IDS deployment and custom signature writing
- SysmonForLinux EDR policy engineering for ransomware detection

### Tools Mastered
- nmap, Hydra, netcat, Metasploit concepts
- Suricata, Sysmon, iptables, UFW
- Docker, The Sleuth Kit, Volatility concepts
- Kibana/ELK Stack, Wireshark concepts
- Python scripting for security automation

---

## Phase 1 Reflection

Starting Phase 1 with no background in cybersecurity and ending it
able to run a full breach investigation — from reconnaissance through
exploitation through forensics and defense — has been the most
technically intensive learning experience I have had. The most
important shift in my thinking came from doing both sides of every
operation: once you have exploited a Redis instance with no password
or cracked an SSH credential from a wordlist, you understand
immediately why those controls matter in a way that no lecture
could teach. The TEPP capstone brought all of it together — three
networks, four phases, every skill from the phase in one operation.
The biggest lesson I am taking into Phase 2 is that defense is not
about stopping every possible attack; it is about making your
environment expensive enough to attack that adversaries move on.