# 문제 : 1+3+6+10+15+……의 순서로 10번째 항까지 합계를 구하라

i = 0
j = 0
sum = 0

while j < 10:
    j += 1
    i += j
    sum += i
    print(sum)

print("answer : ", sum) 