n = 19
Sum = 0
sovuanhap = []
while ( True):
    m = int(input("Nhap vao mot so:"))
    if(m > n):
        print("So ban vua nhap lon hon so can tim")
        if(m not in sovuanhap):
            Sum += 1
            sovuanhap.append(m)
    elif( m < n):
        print("So ban vua nhap nho hon so can tim")
        if(m not in sovuanhap):
            Sum += 1
            sovuanhap.append(m)
    else:
        print(f"Ban nhap chinh xac,so can tim la {n}")
        Sum += 1
        print(f"Ban vua nhap {Sum} lan")
        break