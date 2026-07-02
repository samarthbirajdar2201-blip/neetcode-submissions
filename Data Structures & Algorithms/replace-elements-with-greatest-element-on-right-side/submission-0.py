class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        result  = [0] * n

        rmax = -1

        for i in range (n -1 , -1 ,-1):
            result[i] =  rmax

            rmax = max(arr[i], rmax)
        return result