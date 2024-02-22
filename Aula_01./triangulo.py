import math

print("insira a base do triangulo:")
x= int(input())
print("insira a altura do triangulo:")
y= int(input())

area= x*y
peri= (x*2)+(y*2)

d= math.sqrt((peri**2-(8*area)))

d= d*0.5
print(area, peri, d)
