# Week 11 — Network Defense & Perimeter Hardening
**Focus:** Firewall engineering, IDS deployment, endpoint detection
**Sessions:** S31, S32, S33 + TLAB11
**Dates:** May 18–20, 2026

---

## Session Summaries

### S31 — The Barricade: Firewall Engineering
This session covered host-based firewall configuration using UFW
and raw iptables rules to implement a DMZ architecture. A Default
Deny posture was configured using UFW, allowing only SSH (port 22)
and HTTPS (port 443). Raw iptables rules were then engineered to
restrict lateral movement from a compromised web server — allowing
outbound traffic only to the internal database on port 3306 while
dropping all other connections to the internal subnet (Cheswick
et al., 2003).

### S32 — The Tripwire: Suricata IDS Deployment
This session introduced network intrusion detection using Suricata,
an open-source IDS engine. Two custom signatures were written and
deployed: an ICMP ping detection rule (sid:1000001) and a malware
User-Agent content-matching rule that detected the Ghost_Scanner_v1
threat actor signature in HTTP traffic (sid:1000002). Both rules
were verified by triggering them from inside the sensor container
and confirming alerts in eve.json (Beale et al., 2014).

### S33 — The Last Mile: Endpoint Detection & Response
This session covered SysmonForLinux deployment for granular endpoint
monitoring. A simulated ransomware macro (invoice_macro.ps1) was
executed and analyzed — revealing that it ran vssadmin delete
shadows to destroy Volume Shadow Copies before encryption. An XML
EDR detection policy was engineered to catch this exact ransomware
precursor behavior using a ProcessCreate CommandLine condition,
trapping the attack in the window before encryption begins
(Russinovich et al., 2021).

### TLAB11 — Operation Fortress: Defense in Depth
The capstone deployed all three defensive layers simultaneously
against a known adversary using the 198.51.100.0/24 C2 subnet:
Layer 1 (iptables egress DROP rule) blocked C2 callbacks, Layer 2
(Suricata cmd=whoami signature) detected web shell exploitation,
and Layer 3 (Sysmon CommandLine condition) caught the post-
exploitation payload download. Together these layers implement
true Defense in Depth — each independently stopping a different
stage of the kill chain.

---

## Key Concepts
- Default Deny firewall posture
- DMZ architecture and lateral movement prevention
- Suricata rule syntax and content matching
- Network IDS vs IPS distinction
- Sysmon Event ID 1 process creation monitoring
- Ransomware precursor detection
- Defense in Depth architecture

---

## Artifacts
- `firewall_config.sh` — S31 iptables DMZ lockdown script
- `custom_ids.rules` — S32 Suricata custom signatures
- `edr_policy.xml` — S33 Sysmon ransomware detection policy
- `Operation_Fortress_Report.md` — TLAB11 Defense in Depth report

---

## References
Beale, J., Baker, A., Esler, J., & Northcutt, S. (2014).
*Snort intrusion detection and prevention toolkit*. Syngress.

Cheswick, W., Bellovin, S., & Rubin, A. (2003). *Firewalls and
internet security: Repelling the wily hacker* (2nd ed.).
Addison-Wesley.

Russinovich, M., Solomon, D., & Ionescu, A. (2021).
*Windows internals* (7th ed.). Microsoft Press.
