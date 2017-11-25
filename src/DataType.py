
'''
python Datatypes are:
number, string , lists, tulips and Dictionaties
'''

print('Hello python data types')

grocery_list =['juice','Bread', 'Banana', 'Milk','cerial', 'meat', 'egg']

print('The first itrm is', grocery_list[0])

print(grocery_list[2:5])

grocery_list.append('Orange')

other_tasks = ['wash car','clean garage','cut lawn']

super_list =[grocery_list,other_tasks]

super_list[0].insert(1, 'onion')

super_list[0].append('Apple')

print('the complete list is:', super_list)

sub_list =  super_list[1:3]
print("sub List is :", end="")
print(sub_list)

mergedList = grocery_list + other_tasks

print("Merged List is : ", mergedList)

mergedList.sort()

print("Sorted List is : ", mergedList)

mergedList.reverse()

print("Reverce sorted List is : ", mergedList)

print('lenght of merged list is:', len(mergedList))
print('Max of merged list is:', max(mergedList))
print('Min of merged list is:', min(mergedList))

#mapps and dictionaries

print('------------------------------Persian Kings---------------------------------')

Persian_Kings = {'Akhamenian':'Cyrus The grate', 'Sasanian':
                'Anooshirvan', 'Afsharian' :'NaderShah', 'Safavi' :'Shah Abbas',
                 'ghajaarian': 'Nasereddin Shah'}

print(Persian_Kings)

del Persian_Kings['ghajaarian']

print(Persian_Kings)

Persian_Kings.update({'Pahlavi': 'Reza Shah The Grate'})

print(Persian_Kings)

print("Akhaminnian King is: ",Persian_Kings.get('Akhamenian'))
print('The keys are: ',Persian_Kings.keys())

print('values are:')

print(Persian_Kings.values())
