


#二分法 算法实现 二分法需要是有序的集合，这里使用数组


def search(list,item):
    low=0;
    high=len(list)-1;

    while low <=high:
        mid=int((low+high)/2);
        guess=list[mid];

        if guess==item:
            print(mid)
            return 
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    print('not this number');

myList=[1,3,5,7,9];

search(myList,3);
search(myList,-1);
search(myList,9)


#第二个算法实现









