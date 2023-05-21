# 양의 정수를 입력받고 그 수가 소수인지 아닌지 판별하시오

a = int(input("양의 정수를 입력해주세요 : "))
j = 2

if (a % j == 0):
    
    while (True):
        j = j + 1
        print(j)
        if a == j:
            print("소수")
        else:
            print("소수 아님")


