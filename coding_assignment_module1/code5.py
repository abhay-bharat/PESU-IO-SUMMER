ele = input("Enter input : ")
def is_number(n):
	try:
		float(n)
	except ValueError:
		return False
	return True
	
if is_number(ele):
	print("The string entered is numeric")
else:
	print("The string is not numeric")
