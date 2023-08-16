#All Sorting Algorithms
# Each prints corresponding values at end of each corresponding iteration
#ex print statement - bubbleSort([7, 5, 6, 2, 1])
#must call sort alg at bottom
'''
If asked to describe how a sorting alg works, pull up lecture 11, 12 or 13.py
'''
def bubbleSort(aList): #O-notation is O(n^2)
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                #swap (bubble up)
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
        print(passnum, aList)

def insertionSort(aList): #O(n^2) -- (best case scenario is O(n), list already sorted)
    for index in range(1, len(aList)):
        currentvalue = aList[index]
        position = index

        #shift elements to make room for insertion
        while position > 0 and aList[position - 1] > currentvalue:
            aList[position] = aList[position-1]
            position = position - 1

        # insert element in appropriate place
        aList[position] = currentvalue

        print(index, aList)

def selectionSort(aList): # O(n^2)
    for fillslot in range(len(aList)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location
        #swap largest element in correct place
        temp = aList[fillslot]
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp
        print(fillslot, aList)

### Quick Sort Stuff

#partition fucntion will organize left sublist < pivot and right sublist
# > pivot

def partition(aList, first, last): # O(n)
    pivotvalue = aList[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        # move leftmark until we find a left element > pivot
        while leftmark <= rightmark and aList[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # move rightmark until we find a right element < pivot
        while rightmark >= leftmark and aList[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        # check if were done swapping left/right elements into CORRECT side
        if rightmark < leftmark:
            done = True
        else: # swap left and right elements into correct side of list
            temp = aList[leftmark]
            aList[leftmark] = aList[rightmark]
            aList[rightmark] = temp
    print("pre aList rightmark value swap")
    print("rightmark:", aList[rightmark])
    print(aList)
    #if leftmark <= len(aList) + 1:
        #print("leftmark (if applicable):", aList[leftmark])

    # put pivot value into correct place
    temp = aList[first]
    aList[first] = aList[rightmark]
    aList[rightmark] = temp
    
    print("post aList rightmark value swap")
    print(aList)

    return rightmark

def quickSortHelper(aList, first, last):
    if first < last:

        # will define teh index of the left/right sublists
        splitpoint = partition(aList, first, last)

        # recursively sort the left and right sublists
        quickSortHelper(aList, first, splitpoint-1)
        quickSortHelper(aList, splitpoint+1, last)
        

def quickSort(aList): #O(nlog n) in best case; O(n^2) in worst case, uneven sublists
    quickSortHelper(aList, 0, len(aList)-1)
    
### End of Quick Sort Stuff

def mergeSort(aList): #O(nlog n) with O(n) additional memory required
    if len(aList) > 1:
        mid = len(aList) // 2

        # uses additional space to create left/right halves
        lefthalf = aList[:mid]
        righthalf = aList[mid:]

        #recursive sorts lefthalf, then righthalf lists
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #Merge two sorted sublists (lefthalf/righthalf) int a List
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                aList[k] = lefthalf[i]
                i += 1
            else:
                aList[k] = righthalf[j]
                j += 1
            k += 1
            
        print("i:", i, "j:", j, "k:", k) # move to spot where question corresponds to


        # put remaining lefthalf elements (if they exist) into aList
        while i < len(lefthalf):
            aList[k] = lefthalf[i]
            i += 1
            k += 1
            
        # put remaining righthalf elemtns (if they exist) into aList
        while j < len(righthalf):
            aList[k] = righthalf[j]
            j += 1
            k += 1

'''
Divide and Conquer Algorithms
* Subdivide a larger problem into smaller problms
* Solve each smaller part
* Combine solution of smaller sub problems back into the larger problem
    * Quick Sort's partition step and Merge Sort's merge step have the same
    Big-O running time in all cases (assuming both steps are using
    a Python List with n elements).
Merge Sort
Idea: Break a list into sublists where the size == 1
    * A sublist with 1 element is considered sorted

* Merge each small sorted sublist together to form a sorted larger list
* Coninue to merge ublists into the original list.
* The merge step is 0(n)
* The splitting step is O(log n)
* Entire algorithm is O(nlog n) (consistently)
* BUT! Requires an additional O(n) memory
'''

''' Quick Sort
* Another divide and conquer algorithm
* ew can improve running times to O(nlog n) (like mergesort) in a TYPICAL case,
but we'll also see hw tthis can lead to O(n^2) in a worst case scenario
    * worst case is if sublists are not evenly split
'''

mergeSort([2, 5, 6, 8, 3, 4, 7, 10])

