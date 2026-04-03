#Problem description: You are given a list of cmd_logs. Each entry consists
# of three elements separated by a | character. The format is: “User|Called_Function|Result”.
#This time, we are not looking for an attacker. We want to check which system components users have
#the most trouble with (or which ones they are trying to access illegally).
#Write code that counts the errors and returns a list of function names (e.g., Start-Honey, LabOn)
#that ended with the “FAILED” status two or more times.


cmd_logs = [
    "admin|Start-Honey|SUCCESS",
    "guest|Stop-Honey|FAILED",
    "barto|Show-Honey|SUCCESS",
    "guest|LabOff|FAILED",
    "user1|LabOn|SUCCESS",
    "guest|Stop-Honey|FAILED",
    "admin|Reload-Honey|SUCCESS",
    "hacker|LabOff|FAILED",
    "hacker|Stop-Honey|FAILED"
]

storage = {} #creating new dictionary
for i in cmd_logs:
    account, function, status = i.split("|")
    
    if status == "FAILED": #checks for word "FAILED"
        if function in storage:
            storage[function] += 1
        else:
            storage[function] = 1

errors = [] #list for end-results 

for k,v in storage.items():
    if v >= 2:
        errors.append(f"{k} failed {v} times")
        
print(errors)

      