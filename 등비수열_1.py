# 1+2+4+7+11+…… 의 순서로 10번째 항까지 합계를 구하시오

i = 1
j = 0
sum = 1

while j < 9:
    j += 1
    i += j
    sum += i
    print(sum)

print("answer : ", sum)
