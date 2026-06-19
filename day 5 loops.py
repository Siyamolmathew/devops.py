# 1. Create our list of infrastructure nodes
servers = ["web-prod-01", "db-prod-02", "storage-test-01", "auth-prod-03"]

print("--- STARTING SYSTEM-WIDE AUDIT ---")

# 2. Start the loop. 
# 'server' is a temporary variable that holds the current item in the loop.
for server in servers:
    print(f"Checking compliance status for: {server}...")
    
    # 3. Inside the loop, we use our Day 2 if/else logic!
    if "test" in server:
        print(f" ALERT: {server} is a test node running in a production environment!")
    else:
        print(f" {server} passed security verification.")
        
    print("-" * 30) # Prints a simple divider line between server checks

print("--- AUDIT COMPLETE ---")