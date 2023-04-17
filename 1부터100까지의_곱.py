# 1부터 100까지의 곱을 나타내시오

i = 0
h = 1

while i < 100:
    i += 1
    h = h * i
    print("{0}번째 수 표시 : {1}".format(i, h)) 

print("결과는 {}입니다.".format(h))
