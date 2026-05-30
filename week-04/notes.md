# Week 4 — Virtualization, Virtual Machines & Containers
**Focus:** Docker architecture, secure container configuration, multi-container deployment
**Sessions:** S10, S11, S12
**Dates:** March 30 – April 3, 2026

---

## Session Summaries

### S10 — Virtualization Concepts & Multi-Container Architecture
This session introduced virtualization fundamentals and Docker's
container model, covering how containers differ from virtual machines
in terms of resource isolation and portability. The artifact
docker-compose.yml demonstrates multi-container orchestration,
defining networked services that communicate through isolated Docker
networks — a pattern used in every modern enterprise application
deployment (Kane et al., 2023).

### S11 — Secure Container Configuration
This session focused on hardening Docker containers by minimizing
attack surface — using non-root users, dropping unnecessary
capabilities, and building minimal images. A secured Dockerfile
was engineered to follow the principle of least privilege, ensuring
containers run with only the permissions required for their function
and nothing more (NIST, 2020).

### S12 — Docker Compose Deployment
This session covered deploying a full multi-service stack using
Docker Compose, including a web server, application layer, and
database — simulating a real enterprise environment. The artifact
deploy_web.sh automates the deployment sequence, demonstrating
infrastructure-as-code principles that reduce human error in
production deployments.

---

## Key Concepts
- Container vs virtual machine architecture
- Docker networking and isolated subnets
- Principle of least privilege in container configuration
- Multi-container orchestration with Docker Compose
- Infrastructure as code and deployment automation

---

## Artifacts
- `docker-compose.yml` — Multi-container orchestration definition
- `deploy_web.sh` — Automated deployment script
- `hyperstack_audit.json` — Container security audit output

---

## References
Kane, S., Matthias, K., & Fischer, S. (2023). *Docker: Up and running*
(3rd ed.). O'Reilly Media.

NIST. (2020). *Security and privacy controls for information systems
and organizations* (SP 800-53 Rev. 5). National Institute of
Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
