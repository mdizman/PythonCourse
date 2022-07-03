ogrenciler={
    '120':{
        'ad':'Ali',
        'soyad':'Mert',
        'telefon':'123456789'
        },
    '121':{
        'ad':'Melih',
        'soyad':'Sert',
        'telefon':'654681644'
        },
    '122':{
        'ad':'Ayşe',
        'soyad':'Eren',
        'telefon':'548651962'
        },
    
    }

#Bilggileri verilen öğrencilerin kulanıcıdan aldığı bilgilerle dictionary içinde saklayınız
ogrenciler = {}
 
number = input('Öğrenci No:')
name = input('Öğrenci Adı:')
surname = input('Öğrenci Soyad:')
phone = input('Öğrenci Telefon:') 

ogrenciler[number]= {
    'ad':name,
    'soyad':surname,
    'telefon':phone
}
print(ogrenciler)

# ogrenciler.update({
#     number:{
#         'ad':name,
#         'soyad':surname,         Aynı işlemi yapar 
#         'telefon':phone
#         }
# })
