#Problem description: You are given a list of honeypot_logs. 
# Each log consists of three parts separated by a vertical bar(the so-called pipe: |).
#The format is: “IP_Address|Target_Port|Status”.
#Your task is to write code that finds and returns a list of unique
#IP addresses whose packets were dropped (status “DROPPED”) 3 times or more.

honeypot_logs = [
    "10.0.0.2|80|ALLOWED",
    "192.168.5.50|22|DROPPED",
    "192.168.5.50|23|DROPPED",
    "10.0.0.2|443|ALLOWED",
    "172.16.0.8|21|DROPPED",
    "192.168.5.50|3389|DROPPED",
    "192.168.5.50|80|ALLOWED",
    "172.16.0.8|22|DROPPED",
    "10.0.0.2|22|DROPPED",
    "172.16.0.8|8080|DROPPED"
]

attacker_ip = {}

for i in honeypot_logs: #i takes temporarly each line
    ip,port,status = i.split("|") 
 
    if  status == "DROPPED": 
        if ip in attacker_ip: #if there is "locker" it increments it by 1
            attacker_ip[ip] += 1
        else:
            attacker_ip[ip] = 1 #creates new "locker" if it was not created yet

print(attacker_ip)

dropped_IP = [] #new list, final "storage" for our results

for ip,dropped_count in attacker_ip.items():
    if dropped_count >= 3:
        dropped_IP.append(f"{ip} Dropped: {dropped_count})")
        
print("Dropped packets: ", dropped_IP,dropped_count)
       
            

