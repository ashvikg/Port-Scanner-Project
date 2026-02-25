import socket

# Step 1: Target input
target = input("Enter target (IP or domain): ")

# Step 2: Convert to IP
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target")
    exit()

print(f"\nScanning {target} ({target_ip})")
print("-" * 40)

# Step 3: Scan ports
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScan Complete.")