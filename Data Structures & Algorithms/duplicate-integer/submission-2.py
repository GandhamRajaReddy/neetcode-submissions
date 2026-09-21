class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        freq = {}  # hash map to store counts
        for num in nums:
            if num in freq:
                return True  # duplicate found
            freq[num] = 1
        return False  # no duplicates
          


              


        