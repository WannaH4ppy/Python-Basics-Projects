#Problem description: You are given a list of activity_logs.
#Each entry is a string in a simple format: “User|Command”.
#Your task is to create a dictionary where the key is the user’s name 
#and the value is a list (array) of commands that this person has executed.
#Return and print the finished dictionary 
#(here you don’t need to use a second loop for f-strings; just add print(storage) at the very end).


#{ Expected output
    #'admin': ['Start-Honey', 'LabOff'], 
    #'guest': ['Show-Honey', 'Stop-Honey', 'LabOn'], 
    #'barto': ['LabOn', 'Reload-Honey']
#}


activity_logs = [
    "admin|Start-Honey",
    "guest|Show-Honey",
    "barto|LabOn",
    "guest|Stop-Honey",
    "admin|LabOff",
    "barto|Reload-Honey",
    "guest|LabOn"
]

def group_user_activity(x):
    storage = {}

    for i in x:
        user, function = i.split("|")
        #if user in storage:
            #storage[user].append(function)
         #else:
            #storage[user] = []
            #storage[user].append(function)
        if user not in storage:
            storage[user] = []
        
        storage[user].append(function)
        #above is better because we don't use storage[user] 3 times
    
    return storage

def group_useractivity1(x):
    storage = {} 
    
    for i in x:
        x, y = i.split("|")
        #curr_list = storage.get(x, [])
        #curr_list.append(y) #x = user, y = function
        #storage[x] = curr_list
        storage.setdefault(x, []).append(y)
        
    return storage
    
    
    
wynik = group_user_activity(activity_logs)
for k,v in wynik.items():
    print(f"{k} wywolal: {v}")
print("-------------------------------------------------------")
wynik1 = group_useractivity1(activity_logs)
for k,v in wynik1.items():
    print(f"{k} wywolal: {v}")



    

    
#another way of doing this task is by .get() function


    
    
        