# Week 10 — Digital Forensics & Incident Response (DFIR)
**Focus:** Live triage, memory forensics, disk imaging, SIEM correlation
**Sessions:** S28, S29, S30 + TLAB10
**Dates:** May 11–15, 2026

---

## Session Summaries

### S28 — The Crime Scene: Live Triage & Chain of Custody
This session introduced the first-responder approach to incident
response — performing live triage on a compromised system without
destroying volatile evidence. A quarantined Docker container
simulating an active C2 beacon was investigated using netstat to
identify a Netcat backdoor listening on port 4444 (PID 11).
Cryptographic hashing using MD5 and SHA256 was applied to forensic
evidence files to establish an unbroken chain of custody, ensuring
evidence integrity from collection through analysis (Casey, 2011).

### S29 — The Digital Autopsy: Memory & Disk Forensics
This session covered post-mortem forensic analysis using The Sleuth
Kit. Memory carving with strings and grep revealed a hidden rootkit
process (rootkit_beacon.exe, PID 4444) invisible to the operating
system. Disk forensics using fls enumerated deleted files in a FAT
filesystem image, identifying a deleted Resume.exe at inode 582
via its FAT deletion tombstone (_ESUME.EXE). The icat tool was used
to attempt raw sector recovery of the deleted malware payload
(Carrier, 2005).

### S30 — The Central Nervous System: SIEM Log Correlation
This session introduced SIEM (Security Information and Event
Management) operations using the ELK Stack (Elasticsearch, Logstash,
Kibana). Enterprise logs were queried to reconstruct a full attack
timeline — from initial access via web shell exploitation through
lateral movement to Domain Admin, to data exfiltration of 4.5 GB
over port 443. This mirrors the daily workflow of a Tier 2 SOC
analyst correlating disparate log sources into a coherent incident
timeline (Murdoch, 2018).

### TLAB10 — Operation Phantom Pursuit
The capstone investigation combined all three DFIR disciplines into
one operation: SIEM correlation identified the attacker's entry IP
(198.51.100.44), live triage confirmed an active Netcat C2 beacon
(PID 10, port 4444), and disk forensics recovered the deleted
beacon.exe from inode 582 with infection timestamp
2026-05-21 00:18:35 EDT.

---

## Key Concepts
- Order of volatility in digital evidence collection
- Cryptographic chain of custody (MD5 + SHA256)
- Memory forensics and rootkit detection
- FAT filesystem deletion mechanics and inode recovery
- SIEM log correlation and attack timeline reconstruction
- The six-stage IR lifecycle (PICERL)

---

## Artifacts
- `collection_log.txt` — S28 chain of custody log
- `forensic_findings.md` — S29 disk autopsy findings
- `attack_timeline.csv` — S30 SIEM correlation timeline

---

## References
Carrier, B. (2005). *File system forensic analysis*. Addison-Wesley.

Casey, E. (2011). *Digital evidence and computer crime: Forensic
science, computers, and the internet* (3rd ed.). Academic Press.

Murdoch, S. (2018). *Security information and event management
implementation*. McGraw-Hill.
