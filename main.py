lst=[]
n=int(input("Enter no of elements: "))
print("Enter Numbers: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele) #adding the elements to the array

print(lst)

#implementing the Bubblesort
def BubbleSort(arr):
    n=len(arr)
    for i in range(1,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

#call to Bubblesort
BubbleSort(lst)
print("Sorted array is : ")
print(lst)
