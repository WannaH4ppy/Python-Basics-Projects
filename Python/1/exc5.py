#Problem description: You are given a list of firewall_logs.
#Each log consists of three elements separated by a | character.
#The format is: “Protocol|IP_Address|Action”.

#This time, we are only interested in TCP traffic that was blocked
#(“REJECTED”). We ignore other protocols (e.g., UDP or ICMP), 
#as well as traffic that was allowed through (“ACCEPTED”).

#Your task is to find the IP addresses that have recorded 3 or
#more rejected TCP connections. Return the result as a readable 
#list using f-strings.

firewall_logs = [
    "TCP|10.0.0.5|REJECTED",
    "UDP|192.168.1.15|REJECTED", 
    "TCP|192.168.1.15|REJECTED",
    "TCP|10.0.0.5|ACCEPTED", 
    "TCP|10.0.0.5|REJECTED",
    "TCP|10.0.0.5|REJECTED",
    "ICMP|172.16.0.8|REJECTED", 
    "TCP|172.16.0.8|REJECTED",
    "TCP|10.0.0.5|REJECTED",
    "TCP|172.16.0.8|REJECTED"
]

storage={}
for i in firewall_logs:
    port,ip,status = i.split("|")
    if port == "TCP" and status == "REJECTED":
        storage[ip] = storage.get(ip, 0) + 1 #instead of those 4 lines below!
        #if ip in storage:
            #storage[ip] += 1
        #else:
            #storage[ip] = 1

results = []
for k,v in storage.items():
    if v >= 3:
        results.append(f"{k} has been rejected {v} times")
        
print(results)
        
        
#storage[ip] = storage.get(ip, 0) + 1
#storage.get("10.0.0.5", 0), Argument 1 (key) - this is waht we look for in dictionary
#Argument 2 (value) - this is what you expect to be returned if code won't find key, in our case its 0

#if there is no locker like this python returns 0 and do math (0) + 1 = 1, creates
#the locker