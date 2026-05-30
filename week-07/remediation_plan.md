# CLOUDNANO REMEDIATION PLAN
**Operator:** Melake

## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **Unauthenticated AWS S3 Bucket (Contains Customer PII)**
   * **Justification:** No login needed to access real customer data — anyone who finds the link can take everything. Highest priority.

2. **Remote Code Execution in Apache Struts (Internet-Facing Web Server)**
   * **Justification:** It's public facing and a successful attack hands over full server control. More urgent than the CVSS 10.0 router which nobody can physically reach.

3. **SQL Injection in Login Page (Customer Database Portal)**
   * **Justification:** The login page is public and sits right in front of the customer database. One successful attack could dump or wipe everything.

4. **Cross-Site Scripting (XSS) on Support Forum**
   * **Justification:** Public forum means any visitor can trigger it. Attackers can steal sessions and hijack accounts at scale.

5. **Outdated PHP Version 5.4 (Public Marketing Blog)**
   * **Justification:** No patches since 2015 and the blog is internet-facing. Every known vulnerability is wide open.
