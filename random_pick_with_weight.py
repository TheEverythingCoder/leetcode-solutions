class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr = [0]
        for weight in w:
            self.arr.append(weight+self.arr[-1])

    def pickIndex(self):
        """
        :rtype: int
        """
        # w = [2,2,5]; self.arr (prefix sum) = [0,2,4,9]
        pick = random.randint(0,self.arr[-1] - 1)
        l,r = 0, len(self.arr) - 1
        while l <= r:
            mid = l+(r-l)/2
            if self.arr[mid] == pick: # if pick == 2, return 1
                return mid
            elif pick > self.arr[mid]: # if pick == 3,
                if pick < self.arr[mid+1]: # and pick < 4 (the next element in prefix sum)
                    return mid # return 1
                l = mid + 1 # else, check buckets on the right
            elif pick < self.arr[mid]: # if pick == 1,
                if pick >= self.arr[mid-1]: # if pick > 0 (the previous element in the prefix sum)
                    return mid - 1 # return 0
                r = mid - 1 # else, check buckets on the left
        return -1
            
