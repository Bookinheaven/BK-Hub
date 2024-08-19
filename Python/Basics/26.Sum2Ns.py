def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i
        return []