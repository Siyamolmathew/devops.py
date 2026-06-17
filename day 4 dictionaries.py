# 1. Create a dictionary to define a server profile
server_profile = {
    "hostname": "db-prod-01",
    "ip_address": "10.0.0.15",
    "cpu_cores": 4,
    "is_active": True
}

print("--- INFRASTRUCTURE PROFILE RETRIEVAL ---")

# 2. Accessing values using their specific keys
print(f"Target Hostname: {server_profile['hostname']}")
print(f"Network Location: {server_profile['ip_address']}")

# 3. Dynamically updating an existing value inside a dictionary
server_profile["cpu_cores"] = 8
print(f"🔄 Upgraded Resources! New CPU Cores: {server_profile['cpu_cores']}")

# 4. Adding a brand new key-value pair to the dictionary on the fly
server_profile["environment"] = "production"

# 5. Printing the entire dictionary to see the complete updated structure
print("\nFull Updated Profile Data Object:")
print(server_profile)