#Write a function: def solution(A):
#that, given a list A of N integers, returns the smallest positive integer
#(greater than 0) that does not occur in A.
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 4], the function should return 3.
#Given A = [-1, -3], the function should return 1.

#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..100,000];
#each element of list A is an integer within the range [-1,000,000..1,000,000].

def solution (A):
    
    unique_val = set(A)
    smallest = 1
    while smallest in unique_val:
        smallest+=1
    
    return smallest

A = [1,2,3,4,5,6,7]
print(solution(A))
    

#Write a function: def solution(A):
#that, given a list A of N integers, returns 1 if A is a permutation
# and 0 if it is not. A permutation is a sequence containing each element
#from 1 to N once, and only once.
#For example, given list A = [4, 1, 3, 2], the function should return 1.
#Given list A = [4, 1, 3], the function should return 0.
#Given list A = [1, 2, 2, 4], the function should return 0.
#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..100,000];
#each element of list A is an integer within the range [1..1,000,000,000].


def solution1 (A):
    unique_values = set(A)
    if len(unique_values) == len(A) and max(unique_values) == len(A):
        return 1
    else:
        return 0
    
A = [10,9,8,7,6,5,4,2,3]
print(solution1(A))
        
        