class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, (len(matrix) * len(matrix[0])) - 1
        n = len(matrix[0])
        while l<=r:
            mid = (l+r) // 2
            val = matrix[mid //n][mid % n]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        