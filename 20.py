a = [1, 3, 5, 30, 42, 43, 500]
def search(a, n):
    for i in a:
        if n==i:
            print(f"{n} found at {i} in list.")
        else:
            print("Not found.")

def binary_search(a, n):
    start=1
    end=len(a)-1
    while True:
        mid_index=(end-start)//2
        if mid_index<start or mid_index>end or mid_index<0:
            print("Not found.")
            break
        
        mid_element=a[mid_index]
        if mid_element==n:
            print(f"{n} found at {mid_index}.")
            break
        elif mid_element<n:
            end=mid_index
        else:
            start=mid_index

import tracemalloc
tracemalloc.start()
search(a, 43)
print(tracemalloc.get_traced_memory())        