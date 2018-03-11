'''
program to find the build order
projects : a,b,c,d,e,f
dependencies : (a,d) , (f,b), (b,d), (f,a), (d,c)
output : f, e, a, b, d,c
'''

def getOrder(dMat,node,order,visited):
    visited.append(node)
    for i in dMat[node]:
        if i not in visited:
            getOrder(dMat,i,order,visited)
    order.append(node)

def buildOrder(dMat):
    visited = []
    order = []
    for i in range(len(dMat)):
        if i not in visited:
            getOrder(dMat,i,order,visited)
    printOrder(order)
def printOrder(order):
    for i in order:
        print chr(97+i),

def main():
    dependencyMat = [[5],[5],[3],[0,1],[],[]]
    buildOrder(dependencyMat)

if __name__=="__main__":
    main()
