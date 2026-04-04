#Example of linear-search, this is complexity of time
#N is the list of elements in collection (len(scope))
#Notation Big O always describes the worst case scenario 

#it has a big pros because it dont care if data is sorted or not, it will alwyas
#find the result once it iterates thorugh all possibilities 

def linear_function(scope, target):
    for i in range(len(scope)):
        if scope[i] == target:
            return i  
    return "Not in scope"
            
            
lista = [1,2,3,4,5,6,7,8]
print(linear_function(lista, 9))