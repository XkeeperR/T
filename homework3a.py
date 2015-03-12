~                                                                                                                                                                                                     
~                                                                                                                                                                                                     
~                                                                                                                                                                                                     
"homework3b.py" 44L, 715C written                                                                                                                                                                     
 
Bradys = ['Mike', 'Carol', 'Marsha', 'Jan', 'Cindy', 'Greg', 'Peter', 'Bobby', 'Alice']
 
print Bradys
print len(Bradys)
 
numBradys = len(Bradys)
counter = 0
 
while counter < numBradys:
        print Bradys[counter]
        counter = counter + 1
 
# another way to print items in list each in separate line
# for x in Bradys:
#       print x
 
# Sorted list
# for sort to work need to use [] istead of () !!!!
 
Bradys.sort()
 
print Bradys
 
# For Loop
 
counter = 0
 
while counter < numBradys:
        print Bradys[counter]
        counter = counter + 1
 