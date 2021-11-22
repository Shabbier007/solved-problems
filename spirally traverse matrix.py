def spirallyTraverse(self, matrix, r, c):
    # code here
    top, down, right, left = 0, r - 1, c - 1, 0
    dir_ = 0
    res = []
    while top <= down and left <= right:
        if dir_ == 0:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
        elif dir_ == 1:
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1
        elif dir_ == 2:
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
        elif dir_ == 3:
            for i in range(down, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        dir_ = (dir_ + 1) % 4
    return res