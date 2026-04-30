from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solução força bruta
        tamanho = len(nums)

        for i in range(tamanho):
            for j in range(i + 1, tamanho):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []