n = int(input("Nhap vao so n:"))
Sum = 0
for number in range(n+1):
    if(number%3==0 or number%5==0):
        Sum += number
print(Sum)