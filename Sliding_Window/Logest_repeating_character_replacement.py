#LeetCode 424
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        count = collections.Counter()

        """ 오른쪽으로 가면서 문자 갯수 추가 """
        for right in range(1,len(s)+1):
            count[s[right-1]] += 1
            max_len = count.most_common(1)[0][1]
            
            """ 윈도우의 길이(right - left)에서 문자의 최대 빈도 수(max_len)를 뺀 값이 k보다 크면 왼쪽에서 이동 """
            if right - left - max_len > k:
                count[s[left]] -= 1
                left +=1
        return right - left
            