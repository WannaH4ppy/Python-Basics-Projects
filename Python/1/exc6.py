#Your task is to find the IP addresses that attempted to specifically 
# target the “Firewall_API” module and were blocked (“BLOCKED”).
#We want to identify those that have recorded 2 or more such blocks.
# Return the result as a list of f-strings.
#(Remember to use the .get() method for counting instead of if/else!)


lab_logs = [
    "192.168.1.10|Honey_DB|ACCESSED",
    "10.0.0.15|Firewall_API|BLOCKED",
    "10.0.0.15|Firewall_API|BLOCKED",
    "172.16.0.5|Honey_DB|BLOCKED",
    "10.0.0.15|Firewall_API|BLOCKED",
    "192.168.1.10|Firewall_API|BLOCKED",
    "172.16.0.5|Firewall_API|BLOCKED",
    "172.16.0.5|Firewall_API|BLOCKED"
]

storage={}

for i in lab_logs:
    ip, module, status = i.split("|")
    if module == "Firewall_API" and status == "BLOCKED":
        storage[ip] = storage.get(ip, 0) + 1

results = []
for k,v in storage.items():
    if v >= 2:
        results.append(f"{k} zablokowano {v} razy")
    
print(results)