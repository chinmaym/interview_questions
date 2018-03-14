'''
program to  implement paint fill.
'''


def paintFill(colorArray,color,i,j):
    if i==len(colorArray) or j==len(colorArray) or i<0 or j<0 or colorArray[i][j] == color:
        return
    else:
        colorArray[i][j] = color
        paintFill(colorArray,color,i+1,j)
        paintFill(colorArray,color,i-1,j)
        paintFill(colorArray,color,i,j+1)
        paintFill(colorArray,color,i,j-1)

def main():
    colorArray = [[1]*3 for i in range(3)]
    paintFill(colorArray,2,1,1)
    print colorArray


if __name__=="__main__":
    main()
