# 1. Define the reusable function using 'def'
# 'server_name' and 'cpu_load' are parameters (inputs the function expects)
def check_server_health(server_name, cpu_load):
    print(f"--- Running Diagnosis for {server_name} ---")

    if cpu_load > 85:
        print(f"🚨 ALERT: {server_name} is overloaded at {cpu_load}% CPU!")
    else:
        print(f"✅ {server_name} load is stable at {cpu_load}%.")

    print("-" * 35)

# 2. The function is defined, but it won't run until we CALL it!
# Let's call the function 3 different times with different data:


check_server_health("web-prod-01", 92)
check_server_health("db-prod-01", 45)
check_server_health("auth-stage-01", 12)
