def search2D(matrix, target):
    i = 0
    j = len(matrix) - 1
    while i <= j:
        m = (i + j) // 2
        x1 = matrix[m][0]
        x2 = matrix[m][len(matrix[m]) - 1]
        if x1 <= target and x2 >= target:
            arr = matrix[m]
            left = 0
            right = len(arr)
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        elif x1 >= target and x2 >= target:
            j = m - 1
        else:
            i = m + 1
            
    return False
