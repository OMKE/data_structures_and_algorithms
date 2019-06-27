

from QuickSort import quick_sort
from MergeSort import merge_sort


array = [10,21,3,4,25,213, 32, 4, 15, 21]

print("Unsorted array")
for i in array:
    print(i, end=" ")


qs_array = array.copy() # performs shallow copy 

quick_sort(qs_array)

print("\n======== Quick sort ========")
for i in qs_array:
    print(i, end=" ")


ms_array = array.copy()
merge_sort(ms_array)
print("\n======== Merge sort ========")
for i in ms_array:
    print(i, end=" ")