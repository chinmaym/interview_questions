'''
program to find route between two given nodes in a directed graph
'''


def checkRoute(adjMat,node1,node2):
    root = node1
    visited = []
    queue = [root]
    while len(queue) != 0:
        node = queue.pop(0)
        if node == node2:
            return True
        visited.append(node)
        for i in adjMat[node]:
            if i not in visited:
                queue.append(i)
    return False



def main():
    adjMat = [[1,2],[2],[],[4],[1]]
    return  checkRoute(adjMat,3,1)

if __name__=="__main__":
    print main()
