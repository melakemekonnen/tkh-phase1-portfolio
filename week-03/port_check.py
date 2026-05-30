import socket

# Open the target file, extract IPs into a list, and replace the gateway 
with open("/home/melakee/lab_prep/target_intel.txt", "r") as f:
	targets = [line.strip().split(": ")[1] for line in f.readlines()]

my_ip="192.168.64.1"
targets[-1]=my_ip

for ip in targets:
    print(f"--- Checking Server: {ip} ---")

    # Create a socket to knock on the door
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timer so we don't wait forever
    s.settimeout(1)

    # Knock on Port 22 (SSH)
    result = s.connect_ex((ip, 22))

    # 0 means Open, anything else means Closed
    if result == 0:
        print(f"SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f"FAILED: Port 22 is CLOSED on {ip}")

    # Close the connection
    s.close() 

