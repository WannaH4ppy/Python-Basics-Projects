#Binary-search
#in opposite to linear-search the list must be sorted, becasue here
#we compare our "midpoint" to value we are searching for

#algorithm in each step reduces the half of the results making it much 
#more efficient than in linear searching, logarithmic complexity O(logN)

def binary_search(scope,target):
    first_val = 0
    last_val = len(scope) - 1
    while first_val <= last_val:
        mid_val = (first_val + last_val) // 2 #average of left & right scope
        if scope[mid_val] == target: #if content of "locker" is my target?
            return mid_val
        elif scope[mid_val] < target:
            first_val = mid_val + 1
        else:
            last_val = mid_val - 1
    return "Value not in scope"

list_of = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(list_of, 10)
print(f"Value from list is at index: {result}")
             
             
