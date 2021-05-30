# 연속을 중복되는 문자는 제외
def solution(characters):
   result = ""
   result += characters[0]
   for i in range(1, len(characters)):
       if characters[i - 1] != characters[i]:
           result += characters[i]
   return result

#The following i문제08.pys code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")