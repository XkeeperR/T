 
import operator
 
gpas = {'Lassoff':3.12, 'Johnson':2.22, 'Reich':3.59, 'Honeychurch':2.98, 'Maini':3.11, 'Levin':2.88, 'Marcus':2.77, 'Banks':3.71}
 
# print list surname/gpa
 
print '-' * 50
print '-' * 50
 
print gpas
 
print '-' * 50
print '-' * 50
 
for x in gpas:
        print 'Last name:' , x, 'GPA:' , gpas[x]
 
print '-' * 50
print '-' * 50
 
# count average GPA for class
 
gpaSum = sum(gpas.values())
gpaLen = len(gpas)
avg = gpaSum / gpaLen
 
print 'Average GPA for class is:' , avg
 
print '-' * 50
print '-' * 50
 
# best rank based on GPA
 
 
gpasort = sorted(gpas.items(), key=operator.itemgetter(1), reverse=True)
 
# print gpasort
 
counter = 1
 
for x in gpasort:
        print 'Rank #', counter, x[0]
        counter = counter + 1
 