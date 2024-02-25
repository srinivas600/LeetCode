class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(houses)
        def solve(no):
            left = 0
            for i in heaters:
                while left < n and houses[left] <= i + no and houses[left] >= i - no:
                    left += 1
            return left >= n

        left, right = 0, 10 ** 9
        while left <= right:
            mid = (left + right) // 2
            if solve(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
