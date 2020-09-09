# WAP TO READ TWO NUMBERS AND FIND THE LARGEST ONE
print("Enter two numbers:")
a = int (input() )
b = int (input() )
if a == b:
	print("Both are equal")
else:
	if a<b:
		print(b," is greater")
	else:
		print(a," is greater")
