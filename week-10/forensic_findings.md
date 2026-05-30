# FORENSIC FINDINGS REPORT (THE MALWARE AUTOPSY)

### WHO:
* rootkit_beacon.exe (PID 4444) — recovered from memory dump via `strings memdump.raw | grep -i "HIDDEN"`. Identified as a HIDDEN_PROCESS_NO_WINDOW threat actor running with no visible UI, consistent with a rootkit/C2 beacon.

### WHAT:
* Resume.exe — confirmed deleted from disk image `compromised_drive.dd` at inode 582. FAT directory entry shows the classic deletion tombstone `_ESUME.EXE` (first byte replaced with 0xE5), confirming intentional deletion by the attacker.

### WHEN:
* 2026-05-18 04:31:52 EDT — infection timestamp pulled directly from inode 582 metadata via `istat compromised_drive.dd 582`. Created and Written timestamps match, indicating the file was dropped and immediately executed without modification.

### HOW:
* Persistence mechanism: Registry Run Key — `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\rootkit_beacon`. The malware established autorun persistence so that `rootkit_beacon.exe` re-launches at every user login, surviving reboots even after the original `Resume.exe` dropper was deleted to cover tracks. Process was identified running as PID 4444 in memory with no associated window, confirming silent background execution.
