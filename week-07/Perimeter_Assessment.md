# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** Melake
**Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** nginx 1.14.2 — web server on port 80
* **Host 2 (172.88.0.15):** Redis cache database — no open web ports
* **Host 3 (172.88.0.20):** Apache httpd 2.4.66 — web server on port 80

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each)*
* **Web Server 1 Finding (172.88.0.10):** Missing X-Frame-Options header leaves the server open to clickjacking. Tool: Nikto
* **Web Server 2 Finding (172.88.0.20):** HTTP TRACE method is active, exposing session cookies and auth tokens to XST attacks. Tool: Nikto

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire assessment)*
* **Top Priority Remediation:** HTTP TRACE Method Enabled on 172.88.0.20 (OSVDB-877)
* **Justification:** It's public facing and can be exploited right now to steal session tokens and take over accounts — no special conditions needed.
