n = int(input("Enter the integer : "))
sum=0
while(n!=0):
	sum += (n%10)
	n=n//10
print("Sum of digits of integer is : ",sum)
