spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
#IndexError error message if  use  index  exceeds  number of values in list value
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1])
#spam[0][1]= bat
#-1 refers to the last index in a list
#slice spam[1:4]
#del statement
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):#use len to iterate over list
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat#multiple assignments
#enumerate() will return two values
#spam.index('value') to find index of value in list
#main way  tuples  different from lists is tuples, like strings, are immutable.
#Tuples cannot have their values modified, appended, or removed.

#copy(), can be used to make a duplicate copy of a mutable value
# like a list or dictionary, not just a copy of a reference.
#If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
# The deepcopy() function will copy these inner lists as well.