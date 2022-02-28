import heapq
class Solution:
    
    """ Leetcode 406. Queue Reconstruction by Height  """
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        
        """ Max Heap """
        
        for person in people:
            heapq.heappush(heap,(-person[0],person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1],[-person[0],person[1]])
        return result
        
        
