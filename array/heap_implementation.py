'''
Heap implementation
'''


class MaxHeap():
    def __init__(self,arr):
        self.arr = arr
        self.arrLen = len(arr)
        pass
    def heapify(self,cur=0):
        if cur>=self.arrLen:
            return  -1
        left = self.heapify(cur*2+1)
        right = self.heapify(cur*2+2)
        if right >= left and right>self.arr[cur]:
            self.arr[cur],self.arr[cur*2+2] = self.arr[cur*2+2],self.arr[cur]
            self.heapify(cur)
        elif left > right and left>self.arr[cur]:
            self.arr[cur],self.arr[cur*2+1] = self.arr[cur*2+1],self.arr[cur]
            self.heapify(cur)
        return self.arr[cur]

def main():
    arr = [1,6,3,7,2,5,4]
    maxHeap = MaxHeap(arr)
    maxHeap.heapify()
    print maxHeap.arr

if __name__=="__main__":
    main()
