a = [1,2,3]
rel = [[1,1],[2,2],[3,3]]


class RELATION():

    def __init__(self,rel):
        self.rel = rel
        self.adjMat = self.makeAdjMat(rel)

    def makeAdjMat(self,rel):
        relation = self.rel
        matrix = []
        for i in range(len(a)):
            row = []
            for j in range(len(a)):
                row.append(0)
            matrix.append(row)
        for i in relation:
            pos1 = a.index(i[0])
            pos2 = a.index(i[1])
            matrix[pos1][pos2] = 1 
        return matrix

    
    
    def isSymmetric(self):
        for i in range(len(self.adjMat)):
            if self.adjMat[i][i] != 1:
                return False
        return True
    

rel = RELATION([[1,2],[3,2],[3,1]])
print(rel.isSymmetric())
                



