

## 主要用python实现一下三大基本排序算法：
### 一、冒泡排序
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

### 二、选择排序
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
### 三、插入排序
    import random

    def insert_sort(li):
        for i in range(1,len(li)): #把整个数组分为有序区和无序区，默认第0个数是有序的，所以从第1个数到最后一个数为无序区
            #[1,4,2,6,7,5]
            tmp = li[i]  #先把无序区中任意一个数提出来用变量保存
            #tmp = 2
           j = i-1      #把有序区里的最后一个数的下标提取出来
            #j = 1(也就是'4'对应的下标)
           while j >=0 and li[j] > tmp: #当有序区的下标不是比0小的时候，说明有序区有数字，并且无序区提取的数字比有序区最后一个数据大的时候，说明此时顺序是乱的
                li[j+1] = li[j]  #把有序区里的最后一个数和它之后一个数赋值成一样
                #[1,4,4,6,7,5]（此时j的下标仍然没变，还是代表'4'）
                j = j-1          #然后把有序区的下标减1，空出位置
               #[1, ,4,6,7,5](此时的j又回到了‘1’，相当于第二个4位置暂时是空的)
           li[j+1] = tmp        #把提取的数字插到空位里面
                #[1,2,4,6,7,5]

    data=list(range(100))
    random.shuffle(data)
    print(data)
    insert_sort(data)
    print(data)

 使用方法：下载到本地直接用IDE运行或在cmd中python 文件名.py即可

说明：每个排序都已经模拟好了随机数据用来排序，两次print的输出分别是无序列表和排序后的有序列表。


备注：三个算法文件里都已经在每行代码中注释了原理，至于冒泡因为比较好理解，就没有太多注释了。
