from itertools import permutations as pm
from itertools import combinations_with_replacement as cm
arr = [1,2,3,4]

#Permutations with repetition
count = 0
for i in pm(arr):
    print(i)
    count += 1
print(count)


#Permutations without repetition-------------


# per_with_r = [(x,y,z,p) for x in arr for y in arr for z in arr for p in arr]
# print(len(per_with_r))

# per_without_r = [(x,y,z,p) for x in arr for y in arr for z in arr for p in arr if x != y and y != z and z != p and x !=p and x != z and y != p ]
# print(per_without_r)
# print(len(per_without_r))
# ans = []


# def reversal(l1):
#     if len(l1) == 1:
#         return l1
#     if 
#     return 

