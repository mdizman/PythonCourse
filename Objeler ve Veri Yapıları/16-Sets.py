fruits = {'orange','apple','banana'}
# print(fruits)   İndexlenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update['mango','grape']
# fruits.update['mango','grape']   Olşan eleman eklenemez


fruits.remove('mango')
fruits.discard('apple')

fruits.pop()

print(fruits)