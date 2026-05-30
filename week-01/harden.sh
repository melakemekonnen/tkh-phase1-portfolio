#!/bin/bash

# Fix Vault first (Phase 1)
chmod 700 ~/Vault
chmod 600 ~/Vault/secrets.txt

# Fix /etc/shadow (Phase 2)
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow

echo "System hardening complete."
