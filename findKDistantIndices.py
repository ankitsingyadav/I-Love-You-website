def findKDistantIndices(nums, key, k):
    result = []
    key_indices = [i for i, val in enumerate(nums) if val == key]

    for i in range(len(nums)):
        for j in key_indices:
            if abs(i - j) <= k:
                result.append(i)
                break   # No need to check other j's once condition satisfied
    return result



