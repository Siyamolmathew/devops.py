# 1. Define a function that CALCULATES and RETURNS a value
def calculate_storage_used(total_gb, available_gb):
    used_gb = total_gb - available_gb
    percentage_used = (used_gb / total_gb) * 100

    # Send the final calculation back to the main script
    return percentage_used


print("--- AUTOMATED RESOURCE MONITOR ---")

# 2. Call the function and SAVE its returned answer inside a variable
current_usage = calculate_storage_used(500, 150)

print(f"Current Disk Usage: {current_usage}%")

# 3. Now we can use that returned value to make automated decisions!
if current_usage > 80:
    print(" ACTION REQUIRED: Disk space is running low! Triggering log cleanup script.")
else:
    print(" STORAGE HEALTHY: Plenty of disk space available.")
