from Functions import Functions

class Reduction:
    def __init__(self, matrix):
        self.matrix = matrix
        self.functions = Functions(matrix, 0, 0)

    def rref_recursive(self, row=0, column=0):
        rows, columns = len(self.matrix), len(self.matrix[0])

        self.functions.row = row
        self.functions.column = column

        if row >= rows or column >= columns:
            return self.matrix 

        pivot = self.functions.finding_the_pivot_row_index()

        if self.matrix[pivot][column] == 0:
            return self.rref_recursive(row, column + 1) 
        
        self.functions.swapping_two_rows(row, pivot)

        self.functions.making_1()

        self.functions.reducing_other_rows_to_produce_a_column()

        return self.rref_recursive(row + 1, column + 1)

    def get_rref(self):
        self.rref_recursive()
        return self.matrix

