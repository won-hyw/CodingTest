#펠린드롬 간단하게 만들어보기
#모든 조건을 만족하지 못하면, 펠린드롬이 아니다

# 5글자인 경우
a = "neven"
for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
        print("펠린드롬이 아니다")
print("펠린드롬이다")
