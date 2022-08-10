# split input and output
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
X, y = data[:, :-1], data[:, -1]
print(X)
print(y)

# data[:split, :] : 2 dimensions, dat[row, column] eg: data[:2, :], choose 2 row and all colunmns of matrix