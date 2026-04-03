
#Problem description: You are given a list of network logs (as a simple list of strings).
#Each log consists of an IP address and a login status, separated by a colon (e.g., “192.168.1.100:FAILED”). 
#Write code that finds and returns a list of unique IP addresses that have recorded 3 or more failed login attempts (status “FAILED”). 
#The order of the returned IP addresses does not matter. 

logs = [
    "10.0.0.5:SUCCESS",
    "192.168.1.1:FAILED",
    "192.168.1.1:FAILED",
    "10.0.0.5:FAILED",
    "172.16.0.2:FAILED",
    "192.168.1.1:FAILED",
    "192.168.1.1:SUCCESS",
    "172.16.0.2:FAILED",
    "172.16.0.2:FAILED"
]

#dictionaries outputs data in same format {"KEY" : VALUE}
attacker = {}

for i in logs:  #we iterate thorugh all lines
    logs_IP, logs_STATUS = i.split(":") #split into two variables, i is the new content
    
    if logs_STATUS == "FAILED": #checks for "FAILED" string
        if logs_IP in attacker: #if IP has it's own "locker" we increment 1 to counter
            attacker[logs_IP] += 1
        else:
            attacker[logs_IP] = 1 #if IP do not have it's own locker we create one
            
print("Dictionary with result: ", attacker)

blocked_IP = []
for ip, error_count in attacker.items():
    if error_count >= 3:
        blocked_IP.append(ip)
        
print("Attacking IP's are: ", blocked_IP)

