""" 분할 정복 연산자(*,+,-) 기준 좌우 분할, 숫자만 남으면 정복 시작, 기본 단위 리스트 """
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def compute(left,right,op):
            
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l)+op+str(r)))
                    
            return res
        
        if expression.isdigit():
            return [expression] 
        
        results = []
        for i,v in enumerate(expression):
            if v in "*+-": # 분할 정복
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                results += compute(left,right,v)
        return results
                