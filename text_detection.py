import datetime

# Simulated sign-in telemetry that mattches our KQL detection parameters
mock_logs = [
    {"time": datetime.datetime(2026, 10, 13, 8, 0), "user": "alice@company.com", "ip": "192.0.2.1", "result": 50125},
    {"time": datetime.datetime(2026, 10, 13, 8, 1), "user": "alice@company.com", "ip": "203.0.113.5", "result": 50125},
    {"time": datetime.datetime(2026, 10, 13, 8, 2), "user": "alice@company.com", "ip": "198.51.100.42", "result": 50125},
    {"time": datetime.datetime(2026, 10, 13, 8, 3), "user": "alice@company.com", "ip": "192.0.2.1", "result": 50125},
]

def evaluate_credential_stuffing(logs):
    failed_attempts = {}
    for log in logs:
        if log["result"] != 0:
            user = log["user"]
            ip = log["ip"]
            if user not in failed_attempts:
                failed_attempts[user] = {"count": 0, "ips": set()}
            failed_attempts[user]["count"] += 1
            failed_attempts[user]["ips"].add(ip)

    print("--- SIEM DETECTION ENGINE OUTPUT ---")
    for user, data in failed_attempts.items():
        if data["count"] >= 2 and len(data["ips"]) >= 3:
            print(f"[ALERT HIGH] User: {user} | Failed Attempts: {data['count']} | Distinct IPs: {len(data['ips'])} | Source IPs: {list(data['ips'])}")

if __name__ == "__main__":
    evaluate_credential_stuffing(mock_logs)