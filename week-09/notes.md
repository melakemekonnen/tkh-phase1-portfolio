# Week 9 — The Application Layer: Web Application Security
**Focus:** SQL injection, XSS, API security, web application attacks
**Sessions:** S22-S27 (Weeks 8-9)
**Dates:** April 27 – May 6, 2026

---

## Session Summaries

### SQL Injection (SQLi)
This lab covered SQL injection attacks against a vulnerable web
application, progressing from basic tautology-based authentication
bypass to advanced UNION-based data exfiltration. By injecting
malicious SQL into login fields, database schema was enumerated and
sensitive data was extracted without valid credentials. The artifact
sqli_report.txt documents the full attack chain and corresponding
remediations including parameterized queries and input validation
(OWASP, 2021).

### Cross-Site Scripting (XSS)
This lab demonstrated reflected and stored XSS vulnerabilities,
where malicious JavaScript payloads were injected into web pages
and executed in victim browsers. The artifact xss_payloads.txt
documents the payloads used to steal session cookies, demonstrating
how XSS can escalate from a UI annoyance to full session hijacking
(Stuttard & Pinto, 2011).

### API Security Assessment
This lab assessed a REST API for common vulnerabilities including
broken authentication, excessive data exposure, and missing rate
limiting. The artifact api_audit.log documents findings from the
API security review, demonstrating how modern application attack
surfaces extend beyond traditional web pages into API endpoints
that are often less rigorously tested (OWASP, 2023).

### OmniPortal Web Application Assessment
A full web application security assessment of the OmniPortal target,
combining SQLi, XSS, and API vulnerabilities into a comprehensive
penetration test. The artifact OmniPortal_Assessment.md documents
the full findings, risk ratings, and remediation recommendations
in a professional pentest report format.

---

## Key Concepts
- SQL injection attack types and prevention
- Cross-site scripting and session hijacking
- API security testing methodology
- OWASP Top 10 vulnerability categories
- Parameterized queries and input sanitization
- Professional vulnerability reporting

---

## Artifacts
- `sqli_report.txt` — SQL injection lab findings
- `xss_payloads.txt` — XSS payload documentation
- `api_audit.log` — API security assessment log
- `OmniPortal_Assessment.md` — Full web app pentest report

---

## References
OWASP. (2021). *OWASP top ten*. https://owasp.org/Top10/

OWASP. (2023). *OWASP API security top 10*.
https://owasp.org/API-Security/

Stuttard, D., & Pinto, M. (2011). *The web application hacker's
handbook: Finding and exploiting security flaws* (2nd ed.). Wiley.
