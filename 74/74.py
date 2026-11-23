class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def m(num):
            row=int(num/len(matrix[0]))
            col=num%len(matrix[0])
            return [row,col]
        l,r=0,(len(matrix)*len(matrix[0]))-1
        while(l<=r):
            mid=(l+r)//2
            [ROW,COL]=m(mid)
            if(matrix[ROW][COL]==target):
                return True
            elif(matrix[ROW][COL]<target):
                l=mid+1
            elif(target<matrix[ROW][COL]):
                r=mid-1
        return False
