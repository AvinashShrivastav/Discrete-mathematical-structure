per_without_r = [(x,y,z,p) for x in arr for y in arr for z in arr for p in arr if x != y and y != z and z != p and x !=p and x != z and y != p ]
# print(per_without_r)
# print(len(per_without_r))