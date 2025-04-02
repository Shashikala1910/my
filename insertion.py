import matplotlib.pyplot as plt
import time
import sys

def insertion_sort(arr):
    n = len(arr) 
    for i in range(1,n):
        temp=arr[i]
        j=i-1
    while(j>=0 and temp<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
        arr[j+1]=temp
     
st=time.time()
x=[10,70,15,8,80,90,20]
print("Before Sorting using Insertion sort",x)
insertion_sort(x)
print("After Sorting using Insertionsort",x)
size_x=sys.getsizeof(x)
et=time.time()
elap_t=et-st
print("\n time complexity of sorting : ",elap_t)
space=size_x
print("space complexity of program:",space)



x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Insertion sorting- Time Complecity is O(n^2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
