#Problem description: You are given two things:

    #logs – A list of logs in the format “IP_Address|Status”.
    #whitelist – A set of trusted IP addresses that are exempt.

#Your task is to find IP addresses that have 3 or more “FAILED” logs, but ONLY THOSE that are NOT on the whitelist.
#Return the result as a list of strings, e.g., using  f-string.

whitelist = {"10.0.0.1", "10.0.0.2", "192.168.1.200"}

logs = [
    "10.0.0.1|FAILED",
    "192.168.1.15|FAILED",
    "192.168.1.15|FAILED",
    "10.0.0.2|FAILED",
    "10.0.0.2|FAILED",
    "10.0.0.2|FAILED",
    "192.168.1.15|FAILED",
    "172.16.0.5|FAILED",
    "172.16.0.5|FAILED",
    "192.168.1.200|FAILED",
    "192.168.1.200|FAILED",
    "192.168.1.200|FAILED",
    "192.168.1.15|SUCCESS"
]

storage={}

for i in logs:
    ip, status = i.split("|")
    if status == "FAILED" and ip not in whitelist: #checks if its erro AND if IP is not in whitelist
        if ip in storage:
            storage[ip] += 1
        else:
            storage[ip] = 1

results=[]

for k,v in storage.items():
    if v >= 3:
        results.append(f"{k} failed {v} times)")
print(results)