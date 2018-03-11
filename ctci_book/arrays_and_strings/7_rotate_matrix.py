'''
Rotate Matrix mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] . Rotate in place

'''

def rotateMatrix(arr):
    arrSize = len(arr[0])
    for i in range(arrSize):
        for k in range(i,arrSize-i-1):
            temp = arr[arrSize-1-i][arrSize-1-k]
            arr[arrSize-1-i][arrSize-1-k] = arr[arrSize-1-k][i]
            arr[arrSize-1-k][i] = arr[i][k]
            arr[i][k] = arr[k][arrSize-1-i]
            arr[k][arrSize-1-i] = temp
    return arr


def main():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    return rotateMatrix(arr)

if __name__=="__main__":
    print main()
