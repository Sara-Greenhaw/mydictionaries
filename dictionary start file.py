

phonebook = {'Chris':'555-1111','Katie':'555-2222', 'Joanne':'555-3333'}
"""
print()
print('*****  start section 1 - print dictionary ********')
print()
print(phonebook)

print(len(phonebook))

mydictionary = dict(m=8,n=9)

print(mydictionary)




print()
print('*****  end section 1 ********')
print()







print()
print('*****  start section 2 - search dictionary ********')
print()

#print(phonebook["Chris"])

name = 'Chris'

if name in phonebook:
    print(phonebook[name])

else: 
    print ("not found")



print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()


phonebook['Chris'] = '555-4444'

phonebook['Joe'] ='555-0123'

print(phonebook)

#if key exists in dictionary, it will update. If it doesn't exist it will add to dictionary

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Chris']
print(phonebook)




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

for k in phonebook:
    print(k)
    print(phonebook[k])

    #iterates through keys
    #to iterate through values: print(phonebook[k]) --> prints values of dictionary



print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - iterate through values  ********')
print()

for v in phonebook.values():
    print(v)
#dictionary is object, and one of dictionary methods is values. This gives you all the values in the dictionary.
#use for loop to iterate through all the values using values method of dictionary!
print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

#for pair in phonebook.items():
    #print(pair)

for k,v in phonebook.items():
    print(k,v)

#items is method of dictionary
#the pair object is a tuple --> getting both the key and the value
#items method gives you both keys and values

print()
print('*****  end section 7 ********')
print()








print()
print('*****  start section 8 - using random and converting to list ********')
print()




print()
print('*****  end section 8 ********')
print()




"""



