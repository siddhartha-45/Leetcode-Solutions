from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count_1 = Counter(basket1)
        count_2 = Counter(basket2)
        total_count = Counter(basket1 + basket2)
        
        for k in total_count:
            if total_count[k] % 2 != 0:
                return -1
        
        surplus = []
        for k in total_count:
            target = total_count[k] // 2
            if count_1[k] > target:
                surplus.extend([k] * (count_1[k] - target))
            elif count_2[k] > target:
                surplus.extend([k] * (count_2[k] - target))
        
        surplus.sort()
        smallest = min(total_count)
        n = len(surplus)
        cost = 0
        for i in range(n // 2):
            cost += min(surplus[i], 2 * smallest)
        return cost
