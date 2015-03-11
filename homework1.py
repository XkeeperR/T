import math #enables math syntax ie math.sqrt() for square root (druha odmocnina)
 
print "------------------------------------------------------"
print "calculate side C of triangle using pythagorean theorem"
print "------------------------------------------------------"
 
sideA = 12.55
sideB = 17.85
 
sideT = (sideA ** 2) + (sideB ** 2) #content of sqare on side C, used as temp value for calculating square root which equals to lenght of side C 
 
sideC = math.sqrt(sideT)
 
sideD = sideC * sideC #confirmation that sideC was calculated correctly
 
sideCc = sideT ** (1/2.0) #different way to calculate square root without using math syntax, need to use float number for square root value or it will not calculate correctly ie 2.0, 3.0
 
 
print "sideA = " , sideA
print "sideB = " , sideB
print "sideT = " , sideT
print "sideC = " , sideC
print "sideD = " , sideD
print "sideCc = " , sideCc
 
print "---------------------------"
print "Different Math calculations"
print "---------------------------"
 
operand1 = 95
operand2 = 64.5
 
print "95 + 64.5 =" , operand1 + operand2
print "95 - 64.5 =" , operand1 - operand2
print "95 * 64.5 =" , operand1 * operand2
print "95 / 64.5 =" , operand1 / operand2
print "95 % 64.5 =" , operand1 % operand2