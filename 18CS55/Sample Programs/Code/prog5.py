# WAP to illustrate working of simple calculator using elif statement

print("Enter the two operands:")
a = int(input())
b = int(input())
print("Enter the operator:")
op = input()
if op == '+':
	print(a," + ",b," = ",(a+b))
elif op == '-':
	print(a," - ",b," = ",(a-b))
elif op == '*':
	print(a," * ",b," = ",(a*b))
elif op == '/':
	if b == 0:
		print("Invalid operation\nCannot divide a number by 0")
	else:
		print(a," / ",b," = ",(a/b))
elif op == '%':
	if b == 0:
		print("Invalid operation\nCannot divide a number by 0")
	else:
		print(a," % ",b," = ",(a%b))
else:
	print("Invalid operator")

	
