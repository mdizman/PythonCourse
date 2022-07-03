# BMW, Mercedes, Opel, Mazda elemanlarını lsite olarak oluştur
arabalar = ['BMW', 'Mercedes' , 'Opel', 'Mazda']

#Liste kaç elemanlı
result = len(arabalar)

#listenin ilk ve son elemanı
result = arabalar[0]
result =arabalar[3]

#MAzda değerini totoya ile değştir
arabalar[-1] ='Toyata'
result = arabalar

#Mercedes listenin elemanı mı
result= 'Mercedes' in arabalar

#Listenin ilk 3 elemanı al
result = arabalar[0:3]

#Listenin sonuna Renault ekle
arabalar[-1:] = 'Renault'

#liste son elemanı sil
del arabalar[-1]
result = arabalar

# liste elemanlarını tersten yazdır
result = arabalar[::-1]

print(result)