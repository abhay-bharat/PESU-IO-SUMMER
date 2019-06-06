n = int(input("Enter the number of elements : "))
num = []
print("Enter the sorted numbers : ")
for e in range(n):
	val = int(input())
	num.append(val)
ele = int(input("Enter the search element : "))
i=0
l =n
flag =0
while(i<l and flag==0):
	mid = (i+l)//2
	if(num[mid]==ele):
		flag =1
		print("The element is found at index : ",mid)
	elif(ele>num[mid]):
		i=mid+1
	else:
		l=mid
if(flag==0):
	print("Search element not found")
