## ⚙️ Phase 1 — Privilege Escalation
- **Entry Point:** SSH into bastion as low-level user `mercenary`
- **Reconnaissance:** Used `sudo -l` to discover misconfigured sudo permissions
- **Exploit:** Abused `awk` binary via GTFOBins to spawn a root shell
- **Result:** Full root access on bastion server

## 🔄 Phase 2 — Persistence
- **Method:** Installed reverse shell cron job as root
- **Mechanism:** Cron calls back to attacker VM every minute via `/dev/tcp`
- **Result:** Guaranteed persistent access even after connection drops

## 🔀 Phase 3 — Lateral Movement (Pivot)
- **Tool:** Metasploit Framework
- **Method:** 
  - Opened SSH session to bastion via `auxiliary/scanner/ssh/ssh_login`
  - Added route to hidden network via `post/multi/manage/autoroute`
  - Started SOCKS proxy via `auxiliary/server/socks_proxy`
  - Scanned hidden network via `proxychains nmap`
- **Result:** Discovered Redis database on port 6379 at 10.0.10.50

## ��️ Tools Used
| Tool | Purpose |
|------|---------|
| SSH | Initial access to bastion |
| GTFOBins | Privilege escalation reference |
| Cron | Persistence mechanism |
| Netcat (nc) | Reverse shell listener |
| Metasploit | Session management and pivoting |
| ProxyChains | Routing traffic through SOCKS proxy |
| Nmap | Port scanning hidden network |

## 📚 Key Concepts Learned
- **Privilege Escalation** via sudo misconfiguration
- **Reverse Shells** using `/dev/tcp`
- **Persistence** via cron jobs
- **Network Pivoting** through compromised hosts
- **SOCKS Proxying** with Metasploit
- **Living off the Land (LOTL)** techniques

## ⚠️ Disclaimer
This lab was conducted in a controlled, isolated Docker environment for educational purposes only. All techniques demonstrated are for authorized penetration testing education.

## 👤 Operator
**melakee** | Penetration Testing Course | Week 8
---

## References
Engebretson, P. (2013). *The basics of hacking and penetration
testing* (2nd ed.). Syngress.

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011).
*Metasploit: The penetration tester's guide*. No Starch Press.

Stuttard, D., & Pinto, M. (2011). *The web application hacker's
handbook: Finding and exploiting security flaws* (2nd ed.). Wiley.
