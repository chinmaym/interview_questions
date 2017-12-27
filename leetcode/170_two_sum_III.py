


class TwoSum3():

    def __init__(self):
        self.numList = list()

    def pprint(self):
        print self.numList

    def add(self,num):
        self.numList.append(num)

    def find(self,val):
        remList = list()
        for i in self.numList:
	    if i in remList:
		return True
	    remList.append(val-i)
	return False

if __name__=="__main__":
    myList = TwoSum3()
    myList.add(1)
    myList.add(3)
    myList.add(5)
    myList.pprint()
    print myList.find(4)
    print myList.find(7)
    print myList.find(6)
