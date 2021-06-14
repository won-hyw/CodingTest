from 문제09 import solution

s = "pPooyY"

# def solution(s):
#     pNum = s.count('p') + s.count('P')
#     yNum = s.count('y') + s.count('Y')
#     if pNum == yNum:
#         return True
#     else:
#         return False

def solution(s):
    pNum = 0
    yNum = 0
    for x in s:
        if x == 'p' or x == 'P':
            pNum += 1
        elif x == 'y' or x == 'Y':
            yNum += 1
    if pNum == yNum:
        return True
    else:
        return False

print(solution(s))



