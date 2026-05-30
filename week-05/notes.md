# Week 5 — Identity, Access Management & Windows Enterprise
**Focus:** IAM policy design, Group Policy, Linux-Windows domain integration
**Sessions:** S13, S14, S15
**Dates:** April 6–10, 2026

---

## Session Summaries

### S13 — Security Policy Design, IAM & MFA
This session covered Identity and Access Management fundamentals
including user provisioning, role-based access control, and
multi-factor authentication enforcement in a Windows enterprise
environment. The lab artifact onboard_engineers.ps1 automates
secure user onboarding in Active Directory, enforcing password
policies and MFA requirements that reduce the risk of credential-
based attacks (Microsoft, 2023).

### S14 — Group Policy & Access Control Enforcement
This session focused on Group Policy Objects (GPOs) as a mechanism
for enforcing security baselines across enterprise endpoints.
The artifact gpo_audit.txt documents the audit findings from a
GPO configuration review, identifying misconfigurations that could
allow privilege escalation or policy bypass in a domain environment
(Payne, 2015).

### S15 — Linux-Windows Domain Join & Identity Unification
This session covered integrating Linux systems into a Windows
Active Directory domain using Winbind and SSSD, enabling centralized
authentication across heterogeneous environments. Unified identity
management reduces the attack surface by eliminating local account
sprawl and ensuring consistent access controls across all systems
regardless of operating system (Garman, 2004).

---

## Key Concepts
- Active Directory user and group management
- Role-based access control (RBAC)
- Multi-factor authentication enforcement
- Group Policy Object configuration and auditing
- Cross-platform identity unification

---

## Artifacts
- `onboard_engineers.ps1` — AD user provisioning automation script
- `gpo_audit.txt` — Group Policy audit findings
- `unified_identity.txt` — Linux-Windows domain join documentation

---

## References
Garman, J. (2004). *Kerberos: The definitive guide*. O'Reilly Media.

Microsoft. (2023). *Active Directory documentation*.
https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/

Payne, C. (2015). *Security without obscurity: A guide to
confidentiality, authentication, and integrity*. CRC Press.
