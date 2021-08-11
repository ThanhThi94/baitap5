import math
a = float(input(3.5))
b = float(input(7))
c = float(input(9))

s = (a+b+c)/2
dien_tich = math.sqrt(s*(s-a)*(s-b)*(s-c))
print (" Diện tích tam giác là: " + dien_tich)