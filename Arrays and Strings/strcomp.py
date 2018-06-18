def ch_comp(str):
	arr = []
	flag = 0
	for i in range(256):
		arr.append(0)
	for j in range(0,len(str)):
		if arr[ord(str[j])] > 1:
			flag = 1
			break
		else : arr[ord(str[j])] += 1
	if flag == 1:
 		print("string has repeated character")



str = raw_input("enter string")
ch_comp(str)
