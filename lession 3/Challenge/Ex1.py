# ax2 + bx + c = 0
a = float(input("nhap vao a: "))
b = float(input("nhap vao b: "))
c = float(input("nhap vao c: "))
print(f"{a}X^2 + {b}X + {c}")

if  (a == 0.0):
    if(b == 0.0):
        if(c== 0.0):
            print("Phương trình vô số nghiệm ")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm duy nhất X =",-c/b )
else:
    delta = b*b- 4*a*c
    if(delta < 0):
        print("phương trình vô nghiệm")
    elif (delta = 0):
        x = float(-b/2*a)
        print(f"Phương trình có một nghiệm duy nhất: {x}")
    else"
        x1 = float(-b - math.sqrt(delta)/(2*a))
        x2 = float(-b + math.sqrt(delta)/(2*a))
        print(f"Phương trình có 2 nghiệm phân biệt: {x1},{x2}")
