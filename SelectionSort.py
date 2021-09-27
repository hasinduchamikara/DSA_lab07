lst=[]
n=int(input("Enter no of elements: "))
print("Enter Numbers: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele) #adding the elements to the array

print(lst)

#Implementing selectionsort
def SelectionSort(A):
    n=len(A)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if A[min_idx]>A[j]:
                min_idx=j
        #swap the found minimum element with the first element
        A[i],A[min_idx]=A[min_idx],A[i]

#Calling to Selection Sort
SelectionSort(lst)
print("Sorted array is : ")
print(lst)