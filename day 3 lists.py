# 1. Create a list of production servers
server_inventory = ["web-server-01", "db-server-01", "auth-server-01"]

print("--- INVENTORY REPORT ---")

# 2. Accessing specific items using their index (Remember: counting starts at 0!)
print(f"Primary Web Node: {server_inventory[0]}")
print(f"Database Node: {server_inventory[1]}")

# 3. Dynamically finding out how many items are in the list using len()
total_servers = len(server_inventory)
print(f"Total active nodes tracked: {total_servers}")

# 4. Adding a new resource to the list using .append()
print("\n🔄 Provisioning new server... Adding to inventory.")
server_inventory.append("backup-server-01")

# 5. Let's print the updated list to verify it's there
print(f"Updated Inventory: {server_inventory}")