from RREF import Reduction

A = [[2,3,4,2],
     [4,6,8,3],
     [1,3,1,4]]

reduction = Reduction(A)
rref_matrix = reduction.get_rref()
print("Reduced Row Echelon Form : ")
for row in rref_matrix:
    print(row)
