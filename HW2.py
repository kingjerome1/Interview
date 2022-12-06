def rebound(x, y):
    x = x / (2 ** y)
    return x 

distance = 100
result = 0

for i in range(11):
    result = result + rebound(distance,i) 
    if i == 10:
        ten_times = rebound(distance,i)
        break

print('總共 ' + str(distance + result))
print('第十次 ' + str(ten_times))
    
