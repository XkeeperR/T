 
# Dictionary
 
age = {'Marek' : 29, 'Martina' : 42, 'Andrea' : 49, 'Stana' : 39 , 'Mama' : 69}
 
# another way to create dictionary, ie blank
#age = dict()
 
print age
 
print '-' *25
print '-' *25
 
print 'Marek is' , age['Marek'], 'years old.'
print 'Andrea is ' , age['Andrea'], 'years old'
 
print '-' *25
print '-' *25
 
# changing value for existing item in dictionary
 
newAge = input('How old is Andrea?')
age['Andrea'] = newAge
 
print age
 
 
print '-' *25
print '-' *25
 
 
# adding new item and its value to the dictionary
 
addName = raw_input('Please type name of family member you want to add:')  #important to use raw_input for text fields or it will not create new item in dictionary in next step
addAge = input('How old is this family member?')
 
age[addName] = addAge # create new item and its value in dicitonary
 
print age
 
print '-' *25
print '-' *25
 
# check for item in dictionary and confirm that its there
 
search = raw_input('Who are you looking for?')
 
if age.has_key(search):
        print search, "is in the dictionary"
else:
        print search, 'is not in dictionary.'