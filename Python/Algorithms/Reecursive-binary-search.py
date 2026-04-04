#SECOND VERSION OF BINARY_SEARCH
#difference lies in function, recursive means that the function calls itself
#Each time the current state is frozen, and function creates a new "storage"
#with new stack (Call Stack), Slicing because that's how we call it is not
#prefered method for searching, it's more memory consuming 

def recursive_binary_search(scope, target):
    if len(scope) == 0: 
        return False 
    else:
        mid_val = (len(scope)) // 2
        if scope[mid_val] == target:
            return True 
        else:
            if scope[mid_val] < target:
                #the reason we +1 it becasue in python [start:stop] works
                #in a way that start (left side is inclusive), and the stop
                #(right side is exclusive)
               return recursive_binary_search(scope[mid_val + 1:], target)
            else: 
               return recursive_binary_search(scope[:mid_val], target)

result = recursive_binary_search(list_of, 12)
print(f"Is the number in the scope?: {result}")


#recursive binary serach works with the problem by itself until it
#has the answer, once it does it works it's way back through the functions
#that called it earlier, from bottom to top
#we can also write this as first (returning values) 
def recursive_binary_search1(scope, target, first_val, last_val):

    if  first_val > last_val:
        return "Out of scope"
    else:
        mid_val = (first_val + last_val) // 2
        if scope[mid_val] == target:
            return mid_val 
        else:
            if scope[mid_val] < target:
                #the reason we +1 it becasue in python [start:stop] works
                #in a way that start (left side is inclusive), and the stop
                #(right side is exclusive)
               return recursive_binary_search1(scope, target, mid_val +1, last_val)
            else: 
               return recursive_binary_search1(scope, target, first_val, mid_val -1)
           
list_of = [10, 20, 30, 40, 50, 60]
#in first go we specify, first - 0 (value) and last - len(list_of) - 1 value
result1 = recursive_binary_search1(list_of, 50, 0, len(list_of) - 1)
print(result1) 