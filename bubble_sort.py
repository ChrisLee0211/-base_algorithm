import random

def bubble_sort(li):
    for i in range(len(li)-1): #整个无序数组的循环，也就是外循环
        for j in range(len(li)-i-1): #随机一组内循环，也就是用来比较的一组数字，是内循环
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

data = list(range(1000))
random.shuffle(data)
print(data)
bubble_sort(data)
print(data)