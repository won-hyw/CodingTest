import math

def solution(scores):
   #여기에 코드를 작성해주세요.
   answer = 0
   scores_len = len(scores)
   answer = sum(scores) - max(scores) - min(scores)
   answer = answer // (scores_len - 2)
   return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [1, 0, 99, 100, 43, 2]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
