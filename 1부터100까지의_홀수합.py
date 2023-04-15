# 1부터 100까지의 홀수 합/짝수 합을 구하시오

i = 1 # i = 1이면 홀수의 합 / i = 0 이면 짝수의 합
sum = 0

while i <= 100:
    sum += i
    i += 2
    # print(sum) 과정 확인

print(sum)