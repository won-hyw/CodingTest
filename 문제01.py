# "S":5%, "G":10%, "V":15%

def solution(price, grade):
    if grade == "S":
        return price - price*0.05
    if grade == "G":
        return price - price*0.1
    if grade == "V":
        return price - price*0.15

'''
# 방식2 : reducedPrice라는 변수를 사용할 때는 elif를 사용해야 한다.(grade가 S일 때 밑에 있는 if문을 체크할 필요가 없기 때문)
def solution(price, grade):
    reducedPrice = 0
    if grade == "S":
        reducedPrice = price - price*0.05
    elif grade == "G":
        reducedPrice = price - price*0.1
    elif grade == "V":
        reducedPrice = price - price*0.15
    return reducedPrice
'''

# testcase를 위한 output
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print("ret1의 값은? ", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)
print("ret2의 값은?", ret2, ".")