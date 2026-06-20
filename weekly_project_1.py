# 1. Our Inventory: A List containing separate Server Dictionaries
server_inventory = [
    {
        "hostname": "web-prod-01",
        "ip": "192.168.1.10",
        "role": "web",
        "status": "online"
    },
    {
        "hostname": "db-prod-01",
        "ip": "192.168.1.20",
        "role": "database",
        "status": "offline"
    },
    {
        "hostname": "auth-stage-01",
        "ip": "192.168.1.30",
        "role": "authentication",
        "status": "online"
    }
]

print("=========================================")
print(" INFRASTRUCTURE SCANNER INITIALIZING... ")
print("=========================================\n")

# 2. Loop through every server profile inside our inventory list
for server in server_inventory:
    print(f"Scanning Target: {server['hostname']} ({server['ip']})")
    # .upper() turns text to UPPERCASE
    print(f"Server Role: {server['role'].upper()}")

    # 3. Check the operational status of the server using if/else logic
    if server["status"] == "online":
        print(" STATUS: OPERATIONAL - Traffic routing active.")
    else:
        print("STATUS: DOWN! - Sending immediate ping request to standby nodes.")

    # Our clean divider line from Day 4!
    print("-" * 40)

print(" ALL TARGET NODES SCANNED. REPORT GENERATED SUCCESSFULLY.")
