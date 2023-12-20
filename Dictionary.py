data = {'id':1, 'name':'sanskar', 'branch':'cse' , 'age':20}
# print(data)

# print(data['id'])

# print(data.get('class','Not found'))    #print "Not Found" if the key 'class' is not there in the dictionary

keys = ['A','B','C']
values = ['Apple', 'Bag', 'Cat']
product = dict(zip(keys,values))

# print(product)

product['D'] = 'Dog'   #Adding a new key with its value in the dictionary
print(product)

del product['D']       #deleting a key with its value from the dictionary
print(product)


