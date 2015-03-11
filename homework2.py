xkeeperr: ~/PFABOnline $ vi homework2.py                                                                                                                                                              
 
import sys
 
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
a3 = int(sys.argv[3])
a4 = int(sys.argv[4])
 
avg = float(a1 + a2 + a3 + a4)/4
 
grade = avg
 
if grade >= 90:
        grade = "Grade A"
elif grade >= 80:
        grade = "Grade B"
elif gradde >= 70:
        grade = "Grade C"
elif grage >= 60:
        grade = "Grade D"
else:   
        grade = "Grade F"
print "-" * 30
print "Your average score is" , avg, "Your grade based on your average is" , grade
print "-" * 30
 