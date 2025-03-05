class Functions:
    def __init__(self, matrix, row, column):
        self.matrix = matrix
        self.row = row
        self.column = column

    def finding_the_pivot_row_index(self):
        pivot = self.row
        number_of_rows = len(self.matrix)
        max_val = abs(self.matrix[self.row][self.column])
        for i in range(self.row, number_of_rows):
            if abs(self.matrix[i][self.column]) > max_val:
                max_val = abs(self.matrix[i][self.column])
                pivot = i
        return pivot

    def swapping_two_rows(self, row_1_index, row_2_index):
        self.matrix[row_1_index], self.matrix[row_2_index] = self.matrix[row_2_index], self.matrix[row_1_index]
    
    def making_1(self):
        pivot_value = self.matrix[self.row][self.column]
        for i in range(len(self.matrix[self.row])):
            self.matrix[self.row][i] /= pivot_value

    def reducing_other_rows_to_produce_a_column(self):
        for i in range(len(self.matrix)):
            if i != self.row:
                factor = self.matrix[i][self.column]
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] = self.matrix[i][j] - factor * self.matrix[self.row][j]
