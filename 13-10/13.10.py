# def matrix(matrixx):
#     return[[row[i] for row in matrixx] for i in range(len(matrixx[0]))]
# matrixx = [[1, 2, 3],[4, 5, 6],[ 7, 8, 9]]
# print(matrix(matrixx))

class Matrix:
    def __init__(self, row):
        self.row = row
        min = len(row[0])
        t = True
        for i in range(len(row)):
            if len(row[i])!=min:
                t = False
        if not t:
            print("не то, но транспонирую")
            
                

    def transpone(self):
        newmatr=[]
        i=0
        for i in range(len(self.row[i])):
            b=[]
            for j in range(len(self.row)):
                b.append(self.row[j][i])
            newmatr.append(b)
        return newmatr



matrix = Matrix([[1, 2, 3],[4, 5, 6],[ 7, 8, 9, 10]])

print(matrix.transpone())



