# Girilen bir sayının  0 - 100 arasında olup olmadığını kontrol edin
sayi = int(input('bir sayi gir :'))
result = 0 < sayi < 100 
print(f'girilen {sayi} sayisi 0 ve 100 aralığında mı :',result)

# girilen bir sayının pozitif çift sayı olup olmadığınıo kontrol ediniz.
sayi = int(input('bir sayi gir :'))
result = (sayi>0) and (sayi%2==0)
print(f'girilen {sayi} sayisi şartları sağlıyor mu:',result)

#e mail ve parola bilgileri ile giriş kontrolü yap
mail='mehmetdizman29@gmail.com'
password=123456
email = input('mail:')
sifre = input('sifre :')

result = sifre==password and email==mail
print(f'girilen {email} maili ve {sifre} sifresi diğer veriler ile eslesiyor mu:',result)

#Girilen 3 sayiyi büyüklük olarak karşılaştırınız
sayi1 = int(input('birinci sayiyi gir :'))
sayi2 = int(input('ikinci sayiyi gir :'))
sayi3 = int(input('ücüncü sayiyi gir :'))
result1 = (sayi1 > sayi2) and (sayi1>sayi3)
print(f'en büyük sayi {sayi1} dir◘',result1)
result2 = (sayi2 > sayi1) and (sayi2>sayi3)
print(f'en büyük sayi {sayi2} dir◘',result2)
result3 = (sayi3 > sayi2) and (sayi3>sayi1)
print(f'en büyük sayi {sayi3} dir◘',result3)

# Dışarıdan girilen kişinin vücut kitle indexi
name = input('Ad :')
kg = float(input('kg:'))
hg = float(input('hg:'))

index = (kg) / (hg)**2
zayif = (index>=0) and index<=18.4
normal = (index>=18.4) and index<=24.9
kilolu = (index>=24.9) and index<=29.9
obez = (index>=29.9) and index<=34.9

print(f'{name} isimli kişinin kilo indeksi : {index} ve kilo değendirmesi zayif:{zayif}')
print(f'{name} isimli kişinin kilo indeksi : {index} ve kilo değendirmesi zayif:{normal}')
print(f'{name} isimli kişinin kilo indeksi : {index} ve kilo değendirmesi zayif:{kilolu}')
print(f'{name} isimli kişinin kilo indeksi : {index} ve kilo değendirmesi zayif:{obez}')