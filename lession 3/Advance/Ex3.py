import datetime

year = input()
if (year == ""):
    year = datetime.datetime.now().year 
n = 0
result = []
for x in range (2019,2019+100):
    if(x % 4 ==0 and x%100 != 0 and n < 10):
        result.append(x)
        n += 1
print(result)