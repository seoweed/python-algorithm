# 버블 정렬 알고리즘 
list = [8,87,1,5,25,4,9,10]
def bubble_sort(list):
    cnt = 0
    while 1:
        for i in range(len(list)-1):
            if list[i] > list[i + 1]:
                a = list[i]
                list[i] = list[i + 1]
                list[i + 1] = a
                cnt += 1
        if cnt > 0:
            cnt = 0
        else:
            return list
            break
    

    

b = bubble_sort(list)
print(b)