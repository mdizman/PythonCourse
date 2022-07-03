# key - value

# 42 -> Konya

sehirler = ['Konya', 'İzmir']
plakalar= [42, 35]

print(plakalar[sehirler.index('Konya')])


plakalar = {'konya':42 , 'İzmir':35}
print(plakalar['konya'])

plakalar['Ankara']=6
plakalar['Kocaeli']='new value'


#---------------------------------------

users={
       'mehmetdizman':{
          'age':22,
          'email':'mehmetdizman29@gmail.com',
          'adres':'Konya'
          },
       
       'alpersoy':{
       'age':22,
       'email':'alpersoy@gmail.com',
       'adres':'Antalya'
       }
    
}
print(users['mehmetdizman'])