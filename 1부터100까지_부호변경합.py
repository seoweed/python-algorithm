# 문제 : 1-2+3-4+5-6+……+99-100 합계를 구하시오

i = 0
sum = 0

while i < 100:
    i += 1
    if i % 2 == 1:
        sum += i
    else:
        sum -= i
print(sum)