# Find the maximum in the left and right triangles
# formed by both diagonals (diagonals included)

n = int(input())  # size of the square matrix
matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
mx = matrix[-1][-1]  # bottom-right element belongs to the area
for i in range(n):
    for j in range(n):
        # left triangle or right triangle
        if n - 1 - j >= i >= j or n - 1 - j <= i <= j:
            mx = max(mx, matrix[i][j])
print(mx)