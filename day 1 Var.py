# 1. Storing configuration data in variables
server_name = "web-prod-01"
environment = "production"
current_memory_usage = 74

# 2. Printing clean status messages using f-strings
print("--- DEVOPS ENGINE INITIALIZING ---")
print(f"Deploying to {environment} environment on server: {server_name}")
print(f"⚠️ WARNING: Current memory load is {current_memory_usage}%")
