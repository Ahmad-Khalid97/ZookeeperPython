# put your python code here
num = int(input())
num_sum = 0
while num > 0:
    num_sum = num_sum + (num % 10)
    num = num // 10
print(num_sum)
