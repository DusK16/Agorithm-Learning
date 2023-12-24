#选择排序

#选择排序的函数
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0                        #index为索引，存储最小元素
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

#编写排序算法
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

#实践
print("The array after sorting is: ",selectionSort([2,8,4,21,32,213894,12,768,4232,121]))
