def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int] (only 0 or 1)
    :rtype: int
    """
    ConsecutiveOnes = 0
    MaxConsecutiveOnes = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ConsecutiveOnes += 1
        else:
            ConsecutiveOnes = 0
        if ConsecutiveOnes > MaxConsecutiveOnes:
            MaxConsecutiveOnes = ConsecutiveOnes
    return MaxConsecutiveOnes
