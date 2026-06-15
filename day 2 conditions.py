# 1. Simulate a system metric resource percentage
cpu_usage = 91

print("--- SYSTEM HEALTH CHECK ---")

# 2. Start the decision-making process
if cpu_usage > 90:
    print("🚨 CRITICAL ALERT: CPU load is dangerously high! Triggering auto-scaling.")
elif cpu_usage >= 75:
    print("⚠️ WARNING: CPU load is elevated. Sending an alert email to the DevOps team.")
else:
    print("✅ HEALTHY: CPU load is normal. No action required.")
