# 1에서 100까지의 자연수 중 홀수 제곱의 합을 구하시오

# answer1

i = 1
sum1 = 0

while i <= 100:
    sum1 = sum1 + (i * i)
    i += 2
 
print("answer1 출력 : ", sum1)

# answer2
j = 0
sum2 = 0

while j < 100:
    j += 1
    if j % 2 == 0:
        pass
    else:
        sum2 = sum2 + (j * j)
        

print("answer2 출력 : ", sum2)

 