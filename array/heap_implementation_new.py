'''
Heap implementation
'''

class heap:
    def __init__(self, arr):
        self.arr = arr
        self.arrLen = len(self.arr)

    def heapify(self, cur = 0):
        left = 2*cur+1
        right = 2*cur+2
        largest = cur
        if left < self.arrLen and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.arrLen and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != cur:
            self.arr[cur], self.arr[largest] = self.arr[largest], self.arr[cur]
            self.heapify(largest)


if __name__=="__main__":
    numArr = [1,23,12,9,30,2,50]
    heapObj = heap(numArr)
    for i in range(heapObj.arrLen/2,-1,-1):
        heapObj.heapify(i)
    print heapObj.arr
