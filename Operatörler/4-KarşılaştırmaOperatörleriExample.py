# Girilen iki sayıdan hangisi büyüktür 
a = int(input('a:'))
b = int(input('b:'))
result = (a>b)
print(f'a: {a} b: {b} den büyüktür :{result}')

# kulanıcıdan iki vize ve final notu alıp ortalama hesaplayınız
vize1 = float(input('1.vize:'))
vize2 = float(input('2.vize:'))
final = float(input('final:'))
ortalama= ((vize1+vize2)*0.6 + (final*0.4))
print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz : {ortalama>50}')

#Girilen sayı tek mi çift mi 
a = int(input('a:'))
result = ((a%2)==0)
print(result)

# Girilen bir sayının negatif durumunu komtrol et
a = int(input('a:'))
result = (a<0)
print(f'sayınız 0 dan küçük mü: {result}')

# PArola ve mail bilgisini isteyip doğruluğunu kontrol ediniz

email = 'mehmetdizman29@gmail.com'
password= '123456'

girilenmail = input('email:')
girilensifre = input('password:')

isEmail = (email == girilenmail)
isSifre = (password == girilensifre)
print(f'E mail bilgisi doğru mu : {isEmail}  parola doğru mu : {isSifre}')