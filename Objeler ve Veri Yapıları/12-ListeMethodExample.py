names = ['Ali','Alp','Melek','Aslı']
years = [1998,2000,1985,2002]

# Cenk ismini names e ekle
names.append('Cenk')

#Sena ismini liste başına ekle
names.insert(0,'Sena')

#Ali ismini listeden sil
names.remove('Ali')

#Alp isminin indexi nedir
print(len(names['Alp']))

# Melek listenin bir elemanımıdır
result = 'Melek' in names
result = names.index('Melek')
#liste elemanlarını ters çevir
names.reverse()
years.reverse()

# liste elemanlarını alfabetik olarak sırala
names.sort()

# Years ı rakamsal büyüklüğe göre sırala
years.sort()

#str = "Chevrolet, DAcia" karakter dizisini listeye çevir
str = "Chevrolet, DAcia"
result=str.split(',')

# years içindeki en büyük ve en küçük
min = min(years)
max = max(years)

#years diziside kaç tane 1998 değeri var
result = years.count(1998)

# years tüm elemanlaroı sil
years.clear()

# kulanıcıdan alınacak 3 marka bilgisini listede saklayın
markalar=[]
marka=input("marka:")
markalar.append(marka)
print(markalar)