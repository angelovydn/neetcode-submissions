class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [2, 3, 5, 8, 15]
        # Target: 13
        # 1-indexed

        _map = defaultdict(int)

        for i,num in enumerate(numbers):

            if num not in _map: _map[num] = i

            diff = target-num

            if diff in _map:
                if i != _map[diff]: return [_map[diff]+1,i+1]

            