class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        # g, s 정렬
        g.sort()
        s.sort()
        i,j =0,0
        
        # 반복문 => 포인터가 리스트의 길이를 넘으면 안됨
        while i <= len(g)-1 and j <= len(s)-1 :
            if s[j] >= g[i]:
                # 아이가 만족하는 최소 쿠키의 크기 일때 +1
                ans +=1
                j +=1
                i+=1
            else:
                # 다음 쿠키로 이동
                j += 1
        return ans
