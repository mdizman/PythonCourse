name='Mehmet'
surname='Dizman'
age=22
#print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {} {} and I am {} years old.'.format(name, surname,age))

result=200/700
print('the result is {}'.format(result))
print('the result is {r:5.4}'.format(r=result)) # 5 koyulan boşluk sayısı 4 de virgülden sonra kaç basamak olması gerektiği

print(f"My name is {name} {surname} and I am {age} years old.") # f string