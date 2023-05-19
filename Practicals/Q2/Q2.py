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
            row = a.index(i[0])
            col = a.index(i[1])
            matrix[row][col] = 1 
        return matrix

    
    
    def isReflexive(self):
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat)):
                if i == j and self.adjMat[i][j] != 1:
                    return False
        return True
    
    def isSymmetric(self):
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat)):
                if self.adjMat[i][j] == 1 and self.adjMat[j][i] != 1:
                    return False
        return True
    
    #This function is just for demo purpose. It has very high time complexity hence it is needed to be changed
    def isTransitive(self):
        for i in range(len(rel.adjMat)):
            for j in range(len(rel.adjMat)):
                for k in range(len(rel.adjMat)):
                    if rel.adjMat[i][j] == 1 and rel.adjMat[j][k] == 1 :
                        if rel.adjMat[i][k] != 1:
                            return False
        return True

    

rel = RELATION([[1,1],[2,2],[3,3],[2,1],[1,2],[2,3]])
print(rel.isReflexive())
print(rel.isSymmetric())
print(rel.isTransitive())
                



