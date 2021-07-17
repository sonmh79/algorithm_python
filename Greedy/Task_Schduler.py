import collections
class Solution:
    """ Leetcode 621 fuxxing hellllll  """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                
            if not counter:
                break
            
            result += n - sub_count + 1
            
        return result
