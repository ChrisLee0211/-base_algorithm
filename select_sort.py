import random

def select_sort(li):
    for i in range(len(li)-1):  #第一趟循环排出有序数列
        min_loc = i #设定暂时最小值为无序区间第一个元素
        for j in range(i+1,len(li)):#第二趟排序让min去和无序数列的数作比较找出真正最小值 
            if li[j] < li[min_loc]:
                min_loc = j
            li[i],li[min_loc] = li[min_loc],li[i]

data = list(range(100))
random.shuffle(data)
print(data)
select_sort(data)
print(data)