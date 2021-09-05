def solution(num_apple, num_carrot, k):
    answer = 0 # 주스의 개수 = 사과 3개 + 당근 1개

    # 당근의 갯수가 사과보다 많으면은 주스를 많이 만들 수 있다. 사과 3개 드니까.
    if num_apple < num_carrot * 3: # 당근 * 3의 갯수가 사과보다 크면은
        answer = num_apple // 3 # 사과를 3으로 나눈 몫
    else: # 아니라면
        answer = num_carrot # 당근의 갯수

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0: # 토끼 먹이 - (사과+당근+i)
        if i % 4 == 0:
            answer = answer -1
        i = i + 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 8  # 사과
num_carrot1 = 4 # 당근
k1 = 3 # 토끼 먹이
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
