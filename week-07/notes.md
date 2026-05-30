# Week 7 — The Perimeter
**Sprint 2 | Phase 1: Reconnaissance, Scanning & Vulnerability Analysis**

---

## Overview
Week 7 marks the beginning of Sprint 2 and a complete shift in mindset.
For six weeks I built, configured, and hardened systems. This week I became
the scout — learning how elite security professionals map a target's full
digital footprint before a single exploit is launched.

---

## Sessions

### Session 19 — The Invisible Scout
**Artifact:** `ThreatProfile_CloudNano.md`

Performed a full passive reconnaissance operation against a proxy target
without sending a single packet to their servers. Used Sublist3r to enumerate
subdomains, BuiltWith to fingerprint the tech stack, and HaveIBeenPwned to
check for credential leaks. Compiled all findings into a professional threat
profile for a fictional acquisition target — CloudNano.

**Tools Used:**
- Sublist3r — subdomain enumeration
- BuiltWith — tech stack fingerprinting
- HaveIBeenPwned — credential leak check

---

### Session 21 — The Prioritization Matrix
**Artifact:** `remediation_plan.md`

Deployed a locally vulnerable Docker container and scanned it with Nikto.
Then triaged a 20-item corporate vulnerability report down to the 5 findings
that posed the greatest actual risk using the Risk = Likelihood x Impact
formula. Justified every selection in writing — not by CVSS score alone.

**Tools Used:**
- Nikto — web vulnerability scanner
- Risk = Likelihood x Impact framework

---

### TLAB 7 — Operation Shadow Map
**Artifact:** `Perimeter_Assessment.md`

Performed a full-scope active reconnaissance and vulnerability assessment
against a sandboxed subnet (172.88.0.0/24). Discovered three live hosts
using an Nmap ping sweep, fingerprinted exact software versions, identified
two web servers and one cache database, ran Nikto against both web servers,
and produced a professional perimeter assessment report with a justified
risk triage for the CISO.

**Tools Used:**
- Nmap — host discovery and version scanning
- Nikto — web vulnerability scanning

---

## Key Concepts Learned

**Passive vs Active Reconnaissance**
Passive recon never touches the target — all data comes from third parties.
Active recon sends packets directly to the target and leaves traces in logs.
Both require different tools and different levels of authorization.

**Nmap — Network Mapping**
Nmap can sweep an entire subnet to find live hosts, then interrogate each
one to identify exact software versions and open ports. This builds a
complete picture of a network's attack surface from scratch.

**Nikto — Web Vulnerability Scanning**
Nikto probes web servers for misconfigurations, missing security headers,
outdated software, and known CVEs. It checks thousands of items in seconds
but produces noisy output — interpreting the results is the real skill.

**Risk = Likelihood x Impact**
A CVSS score alone does not determine real-world priority. A CVSS 10.0 on
an air-gapped server is less urgent than a CVSS 6.0 on a public-facing
server holding customer PII. Context — who can reach it and what happens
if they do — is everything.

**The Cyber Attack Lifecycle — Phase 1**
Reconnaissance is the first phase of every real attack. Understanding how
attackers map targets makes you a better defender because you see what they
see and know what they would hit first.

---

## Artifacts Submitted

| Session | Artifact | Submission |
|---------|----------|------------|
| S19 | ThreatProfile_CloudNano.md | session-submit + git push |
| S21 | remediation_plan.md | session-submit + git push |
| TLAB7 | Perimeter_Assessment.md | session-submit + git push |

---

## The Big Takeaway
The best defense is an offense-informed initiative. Everything this week
was about learning to think like an attacker — mapping, scanning, and
triaging the way a real threat actor would. That knowledge is what makes
a great defender.
---

## References
Hutchins, E., Cloppert, M., & Amin, R. (2011). *Intelligence-driven
computer network defense informed by analysis of adversary campaigns
and intrusion kill chains*. Lockheed Martin.

Shodan. (2024). *Shodan: The search engine for internet-connected
devices*. https://www.shodan.io

Stuttard, D., & Pinto, M. (2011). *The web application hacker's
handbook: Finding and exploiting security flaws* (2nd ed.). Wiley.
