import math
from sympy import *
x = symbols("x")
print("********************************************************************************")
print("De Anza College Winter25\t\tMATH001B\t\tMyat Thit Ko Ko")
print("********************************************************************************")
print("This program calculates the area under a curve, average y-value over two x-values, ", end ='')
print("the length of curve, and volume and surface of solid of revolution around given line.", end ='')
print(" Make sure to input function in correct format.")
print("--------------------------------------------------------------------------------")
print("FORMAT EXAMPLES\n")
print("Logarithm of x to the base e = log(x,E)")
print("Inverse = asin(x)")
print("Algebric = ((4*(x^2)+2)^((3*x^2)*(1/x)))/((7-x)^(1/3))")
print("Trigonometric = sin(x)")
print("Exponential = exp(x)")
print("--------------------------------------------------------------------------------")
print("")
print("********************************************************************************")
y = input("\nEnter a function: ")
y = simplify(y)
print("\nYour input has been simplified.\n")
pretty_print(y)
lowlim = simplify(input("\nEnter lower limit: "))
uplim = simplify(input("Enter upper limit: "))
axis = ""
while axis.upper() != "Y" and axis.upper() != "X": 
    axis = input("Revolve about which axis? ")
n = 100
dx = (uplim - lowlim)/n
xi = []
for i in range (n+1):
    xi.append(lowlim+dx*i)
def NumIntegration(y, xi, dx):
    Sn = 0
    for i in range (len(xi)):
        if i == 0 or i == len(xi)-1:
            Sn = Sn + (y.subs(x, xi[i]))
        elif i%2 == 0:
            Sn = Sn + ( 2 * (y.subs(x, xi[i])))
        else:
            Sn = Sn + (4 * (y.subs(x, xi[i])))
    Sn = (Sn * dx) / 3
    return Sn
Area = (NumIntegration(y, xi, dx))
print("\nArea is", Area.evalf() , "units squared.")
Av = Area * (1/(uplim - lowlim))
print("Average value of the curve is", Av.evalf() , "units.")
Lq = (1+((diff(y,x)) ** 2)) ** 0.5
Length = (NumIntegration(Lq, xi, dx))
print("Length of the curve is", Length.evalf() , "units.")
Sq = 2 * pi * y * Lq
SurfaceArea = (NumIntegration(Sq, xi, dx))
Xq = x * y
CenterX = NumIntegration(Xq, xi, dx) / Area
Yq = y ** 2
CenterY = (NumIntegration(Yq, xi, dx) * 0.5) / Area
print("Centroid is at", end = " (")
print(CenterX.evalf(), end = ", ")
print(CenterY.evalf(), end = ")\n")
if axis.upper() == "Y":
    Revolution = simplify(input("\nRevolve around x = "))
    SolidOfRevolution = 2 * math.pi * abs(CenterX-Revolution) * Area
else:
    Revolution = simplify(input("\nRevolve around y = "))
    SolidOfRevolution = 2 * math.pi * abs(CenterY-Revolution) * Area
SolidOfRevolution = abs(SolidOfRevolution.evalf())
print(f"Volume of the solid of revolution around {axis} axis is {SolidOfRevolution} units cubed")
print(f"Surface area of surface of revolution around {axis} is", abs(SurfaceArea.evalf()), "units squared")
