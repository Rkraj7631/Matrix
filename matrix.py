class Matrix:
    def __init__(self,arr1,arr2):
        self.arr1=arr1
        self.arr2=arr2
        self.addition_of_matrix=[]
        self.sub_of_matrix=[]
        self.multi_of_matrix=[]

    def add_matrix(self):
        for i in range(len(self.arr1)):
            row=[]
            for j in range(len(self.arr1[0])):
                row.append(self.arr1[i][j]+self.arr2[i][j])
            self.addition_of_matrix.append(row)

    def sub_matrix(self):
        for i in range(len(self.arr1)):
            row=[]
            for j in range(len(self.arr1[0])):
                row.append(self.arr1[i][j]-self.arr2[i][j])
            self.sub_of_matrix.append(row)    

    def mul_matrix(self):
        row_a=len(self.arr1)
        col_a=len(self.arr1[0])
        row_b=len(self.arr2)
        col_b=len(self.arr2[0])

        if col_a != row_b:
            print("matrix multiplication not possible")
            return
        
        for i in range(row_a):
            row=[]
            for j in range(col_b):
                sum=0
                for k in range(col_a):
                    sum+= self.arr1[i][k]*self.arr2[k][j]
                row.append(sum)
            self.multi_of_matrix.append(row)

    def display(self):
        print("----Addition of 3x3 matrix----\n")
        for r in self.addition_of_matrix:
            print(r)

        print("---Substraction of 3x3 matrix----\n")
        for t in self.sub_of_matrix:
            print(t)
              
        print("----multiplication of 3x3 matrix----\n")
        for s in self.multi_of_matrix:
            print(s)
                    

def input_matrix():
    matrix=[]
    for i in range(3):
        row=list(map(int,input(f"enter row {i+1} (3 values): ").split()))
        matrix.append(row)
    return matrix

print("Enter Matrix 1 : ")
arr1=input_matrix()

print("Enter Matrix 2 : ")
arr2=input_matrix()

m=Matrix(arr1,arr2)
m.add_matrix()
m.sub_matrix()
m.mul_matrix()
m.display()
