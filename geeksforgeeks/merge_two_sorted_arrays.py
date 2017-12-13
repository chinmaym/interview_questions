'''
Input :  arr1[] = { 1, 3, 4, 5}  
         arr2[] = {2, 4, 6, 8}
Output : arr3[] = {1, 2, 3, 4, 5, 6, 7, 8}
'''




def main():
	arr1 = [1, 3, 4, 5]
	arr2 = [2, 4, 6, 8]
	arr3 = []
	arr1Len = len(arr1)
	arr2Len = len(arr2)
	j = 0; k = 0
	for _ in range(arr1Len+arr2Len-1):
		if j<arr1Len and k<arr2Len:
			if arr1[j]<arr2[k]:
				arr3.append(arr1[j])
				j+=1
			else:
				arr3.append(arr2[k])
				k+=1
		elif j<arr1Len:
			arr3.append(arr1[j])
			j+=1
		else:
			arr3.append(arr2[k])
			k+=1
	return arr3
if __name__=="__main__":
	print main()