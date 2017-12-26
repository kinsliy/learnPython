

#快速排序 关于算法的快慢，大O法，记得快速排序

#的平均情况是O（nlogn）,关于算法时间的计算 去看书，

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
       pivot=arr[0];
       less=[i for i in arr[1:] if i<=pivot] 
       more=[i for i in arr[1:]if i >pivot] 
       return quicksort(less)+[pivot]+quicksort(more)



print(quicksort([10,5,2,3]))