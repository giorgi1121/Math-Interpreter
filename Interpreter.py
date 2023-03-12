#create variables x, y, z
x, y, z = input().split()

#convert x into float
flt_x = float(x)

#convert z into float
flt_z = float(z)

#print calculation with using conditionals
if y == "+":
    print(flt_x + flt_z)
elif y == "-":
    print(flt_x - flt_z)
elif y == "*":
    print(flt_x * flt_z)
else:
    print(flt_x / flt_z)
