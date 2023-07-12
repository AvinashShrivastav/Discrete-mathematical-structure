# Create a class SET. Create member functions to perform the following SET operations:
# 1) ismember: check whether an element belongs to the set or not and return value as
# true/false.
# 2) powerset: list all the elements of the power set of a set .
# 3) subset: Check whether one set is a subset of the other or not.
# 4) union and Intersection of two Sets.
# 5) complement: Assume Universal Set as per the input elements from the user.
# 6) set Difference and Symmetric Difference between two sets.
# 7) cartesian Product of Sets.
# Write a menu driven program to perform the above functions on an instance of the SET
# class.

class SET():
    def __init__(self, lst) :
        self.set = set(lst)

    def isMember(self,element):
        if element in self.set:
            return True
        return False
    
    def powerSet(slef):
        pass

    def isSubsetOf(self, otherset):
        for ele in self.set :
            if ele not in otherset.set:
                return False
        return True

    def setUnion(self, otherset):
        unionSet = set()
        for i in self.set:
            unionSet.add(i)
        for j in otherset.set:
            unionSet.add(j)
        return unionSet
    
    def setIntersection(self, otherset):
        intersect = set()
        for i in self.set:
            if i in otherset.set:
                intersect.add(i)
        for j in otherset.set:
            if j in self.set:
                intersect.add(j)
        return intersect
    
    def complement(self):
        universalSet = eval(input("Enter Universal Set : "))
        compl = set()
        for i in universalSet:
            if i not in self.set:
                compl.add(i)
        return compl
    
    def setDifference(self, otherset):
        diff = self.set.copy()
        intersection = self.setIntersection(otherset)
        for ele in intersection:
            diff.discard(ele)
        return diff
    
    def symmetricDifference(self, otherset):
        union = otherset.setUnion(self)
        intersection = otherset.setIntersection(self)
        for i in intersection:
            union.discard(i)
        return union
    
    def print(self):
        print(self.set)







        

setA = SET([1,2,3,4,7,12])
setB = SET([4,3,2,1,7,11])

print("setA = ")
setA.print()
print("setB = ")
setB.print()
print("Checking if 11 is member of setA and setB")
print("setA",setA.isMember(11))
print("setB",setB.isMember(11))

print("Union of setA and setB : ")
print(setA.setUnion(setB))

print("Intersection of setA and setB : ")
print(setA.setIntersection(setB))

print("Cheking if setA is subset of setB : ")
print(setA.isSubsetOf(setB))

print("Complement of setA :")
# print(setA.complement())

print("Set Differnece of setA and setB : ")
print(setA.setDifference(setB))

print("Symmentric Difference of setA and setB : ")
print(setA.symmetricDifference(setB))
