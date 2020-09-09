# WAP to find biggest of three numbers using nested if
print("Enter 3 numbers:")
a = int(input())
b = int(input())
c = int(input())
if (a > b):
	if (a > c):
		print(a," Is largest")
	else:
		print(c," Is largest")
else:
	if (b > c):
		print(b," Is largest")
	else:
		print(c," Is largest")
