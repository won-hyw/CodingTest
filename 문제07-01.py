#펠린드롬 간단하게 만들어보기
## 모든 조건을 만족하지 못하면, 펠린드롬이 아니다

# 5글자인 경우
a = "neven"
a = "seven"
if a[0] != a[4]:
    print("펠린드롬이 아니다")
elif a[1] != a[3]:
    print("펠린드롬이 아니다")
else:
    print("펠린드롬이다.")

# i값 0, 1
for i in range(2):
    if a[i] != a[4-i]:
        print("펠린드롬이 아니다")
    print("펠린드롬이다.")

# 7글자인 경우
a = "enevene"
if a[0] != a[6]:
    print("펠린드롬이 아니다")
elif a[1] != a[5]:
    print("펠린드롬이 아니다")
elif a[2] != a[4]:
    print("펠린드롬이 아니다")
else:
    print("펠린드롬이다.")

# i는 0, 1, 2
for i in range(3):
    if a[i] != a[6-i]:
        print("펠린드롬이 아니다")
    print("펠린드롬이다.")
