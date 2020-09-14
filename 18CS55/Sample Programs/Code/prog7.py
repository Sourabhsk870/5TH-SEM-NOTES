# WAP to calculate sum of n natural numbers using while loop
print("Enter the number:")
n = int(input())
i = 1
sum = 0
while (i <= n):
	sum += i
	i = i+1
print("SUM=",sum)
