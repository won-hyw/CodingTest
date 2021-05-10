arr = [2,3,7,1]

# 최소값을 구하기 위한 알고리즘을 작성
최소값 = arr[0]
for x in arr:
    if x < 최소값 :
        최소값 = x

# 최대값을 구하기 위한 알고리즘을 작성
최대값 = arr[0]
for x in arr:
    if x > 최대값 :
        최대값 = x