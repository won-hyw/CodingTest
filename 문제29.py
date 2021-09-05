def solution(day, numbers):
   count = 0
   for number in numbers:
       if number%2 == day%2:
           count += 1
   return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
day = 18
numbers = [1212, 2958, 1979, 4942, 1111]
ret = solution(day, numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
