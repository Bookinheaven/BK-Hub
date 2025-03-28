import base64
import random
from datetime import datetime, timedelta

log_templates = [
    "[INFO] System initialized.",
    "[INFO] Connection to SHIELD server established.",
    "[INFO] Data packet received from remote node.",
    "[INFO] User authentication successful.",
    "[WARN] Unauthorized access attempt detected.",
    "[WARN] Network anomaly detected at node {node}.",
    "[ERROR] Data corruption detected in sector {sector}.",
    "[ERROR] Security key mismatch. Re-authentication required.",
    "[DEBUG] System latency at {latency}ms.",
    "[DEBUG] Data stream anomaly detected.",
    "[DEBUG] Encrypting transmission payload...",
    "[TRACE] Tracking signal from IP {ip_address}.",
]

nodes = [random.randint(100, 999) for _ in range(10)]
sectors = [hex(random.randint(1000, 9999)) for _ in range(10)]
latencies = [random.randint(5, 500) for _ in range(10)]
ips = [f"192.168.{random.randint(0, 255)}.{random.randint(1, 255)}" for _ in range(10)]

log_entries = []
start_time = datetime(2025, 3, 8, 14, 20, 0)

for _ in range(200):  
    log_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
    template = random.choice(log_templates)
    
    template = template.replace("{node}", str(random.choice(nodes)))
    template = template.replace("{sector}", str(random.choice(sectors)))
    template = template.replace("{latency}", str(random.choice(latencies)))
    template = template.replace("{ip_address}", str(random.choice(ips)))

    log_entries.append(f"{log_time} {template}")
    
    start_time += timedelta(seconds=random.randint(1, 60))

hidden_message = "its more than pixels, Try e___tool"
encoded_message = base64.b32encode(hidden_message.encode()).decode()
insertion_index = random.randint(30, 90)  
log_entries.insert(insertion_index, f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} [DEBUG] {encoded_message}")

log_file_path = "./hawkeye_log.txt"
with open(log_file_path, "w") as log_file:
    log_file.write("\n".join(log_entries))

print(f"Generated log file with hidden message at: {log_file_path}")
