# 🔐 Network Security Labs

A collection of hands-on Linux security labs completed as part of a cybersecurity fundamentals course. All labs were performed by SSH-ing from a Mac into a Linux VM using VS Code (Remote - SSH extension).

---

## 📚 Table of Contents

- [Session 04 — The Wire (Packet Interrogation)](#-session-04--the-wire-packet-interrogation)
- [Session 05 — Operation Grid Lock (Subnet Blueprint)](#-session-05--operation-grid-lock-subnet-blueprint)
- [Session 06 — Operation Hidden Door (Protocol Audit)](#-session-06--operation-hidden-door-protocol-audit)
- [TLAB W2 — Operation Blackout (Network Remediation)](#-tlab-w2--operation-blackout-network-remediation)

---

## 🔵 Session 04 — The Wire (Packet Interrogation)

### Overview
A hands-on lab focused on diagnosing and restoring network connectivity at the physical, data link, and network layers (OSI Layers 1–3). A sabotage script intentionally downed the primary network interface and removed the default gateway, simulating a real-world remote server lockout scenario.

### 🎯 Objectives
- Diagnose broken network connectivity layer by layer
- Identify a downed network interface using `ip link`
- Restore the interface using `ip link set`
- Verify IP assignment using `ip addr`
- Restore and verify the default gateway using `ip route`
- Validate full connectivity using `ping`
- Recover access via out-of-band console (UTM) after SSH lockout

### 📁 Findings
The sabotage script shut down the `enp0s1` interface and removed the default gateway, immediately killing the SSH session. Recovery was performed via the UTM console by bringing the interface back up with `sudo ip link set enp0s1 up`. The default gateway was automatically restored by DHCP upon interface recovery. Full internet connectivity was confirmed with a successful `ping -c 4 8.8.8.8`.

### 📄 Artifact
All findings documented in `network_audit.txt`.

---

## 🟡 Session 05 — Operation Grid Lock (Subnet Blueprint)

### Overview
A hands-on lab focused on subnet mask misconfiguration and CIDR notation. A sabotage script assigned an overly restrictive `/26` subnet mask that mathematically excluded the gateway (`10.50.50.1`) from the usable host range, isolating the machine from the network.

### 🎯 Objectives
- Analyze IP addresses in binary using Python to understand subnet boundaries
- Use `ipcalc` to calculate host ranges, network IDs, and broadcast addresses
- Identify why a `/26` mask excludes the gateway `10.50.50.1`
- Fix the misconfiguration by expanding the mask to `/24`
- Calculate and document `/27` subnet details for comparison

### 📁 Findings
Binary analysis revealed that `10.50.50.150` (binary `10010110`) and `10.50.50.1` (binary `00000001`) have different first two bits, placing them in separate `/26` networks. The fix involved removing the `/26` address and adding a `/24` mask, expanding the usable range from `10.50.50.129–190` to `10.50.50.1–254`, successfully including the gateway.

### 📄 Artifact
All findings documented in `subnet_blueprint.txt` containing `ipcalc` output for both `/24` and `/27` subnets.

---

## 🔴 Session 06 — Operation Hidden Door (Protocol Audit)

### Overview
A hands-on lab focused on detecting and exposing deception at the protocol layer. A sabotage script tampered with the local DNS override file (`/etc/hosts`) to redirect `google.com` to `127.0.0.1`, and installed a hidden Nginx web service on a non-standard port to simulate an adversary backdoor.

### 🎯 Objectives
- Detect DNS spoofing by auditing `/etc/hosts` for malicious overrides
- Remove fake DNS entries and verify resolution using `dig`
- Discover hidden listening services using `ss -tuln`
- Identify unauthorized services by port analysis and process of elimination
- Extract service fingerprint using `curl -I` headers

### 📁 Findings
The `/etc/hosts` file contained a rogue entry redirecting `google.com` to `127.0.0.1`. After removing the entry, `dig google.com` returned real Google IPs (`64.233.180.x`). A port scan using `ss -tuln` revealed an unexpected service listening on port `8080`. Querying the service with `curl -I localhost:8080` exposed a hidden `nginx/1.28.0 (Ubuntu)` web server — the same server that had been impersonating Google.

### 📄 Artifact
All findings documented in `protocol_audit.txt` containing real Google IPs and the hidden service `Server` header.

---

## 🟠 TLAB W2 — Operation Blackout (Network Remediation)

### Overview
A take-home lab simulating a multi-layer network sabotage and recovery mission. A sabotage script simultaneously misconfigured the subnet mask at Layer 3 and poisoned local DNS at Layer 7, cutting off all primary connectivity. Recovery required pivoting to an Out-of-Band (OOB) console, triaging each layer independently, and providing forensic packet evidence of restored communication.

### 🎯 Objectives
- Pivot to OOB console after intentional SSH lockout
- Identify a `/26` subnet misconfiguration isolating the machine from its gateway (`192.168.10.1`)
- Restore correct `/24` mask and manually re-add the default gateway route
- Detect and remove a malicious `/etc/hosts` entry redirecting `secure.titancorp.com` to `10.99.99.99`
- Restore correct DNS resolution to `192.168.10.193`
- Capture forensic proof of a TCP 3-way handshake using `tcpdump`

### 📁 Findings
The sabotage script assigned `192.168.10.150/26`, placing the machine in the `192.168.10.128–190` block and mathematically excluding the gateway at `192.168.10.1`. After removing the `/26` assignment and re-adding the IP with a `/24` mask, the gateway became reachable. The `/etc/hosts` file contained a rogue entry pointing `secure.titancorp.com` to `10.99.99.99` — a black hole IP. After removing it and adding the correct entry (`192.168.10.193`), DNS resolved correctly. A `tcpdump` capture on the loopback interface confirmed a successful TCP 3-way handshake with the `[S]`, `[S.]`, and `[.]` flags against the target server.

### 📄 Artifact
All findings documented in `tlab_report.txt` containing the restored `ip route` output, cleaned `/etc/hosts`, and `tcpdump` handshake evidence.

---

## References
Forouzan, B. (2007). *Data communications and networking* (4th ed.).
McGraw-Hill.

Sanders, C. (2017). *Practical packet analysis: Using Wireshark to
solve real-world network problems* (3rd ed.). No Starch Press.

Tanenbaum, A., & Wetherall, D. (2011). *Computer networks* (5th ed.).
Prentice Hall.

*Completed as part of a Linux fundamentals & cybersecurity course.*
