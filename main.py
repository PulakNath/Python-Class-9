n = int(input("Enter the number you want to find the sum of: "))
s = 0
i = 1
while i <= n:
    s = s + i
    i += 1
    print(s)
num = int(input("Enter the number you want to check: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
