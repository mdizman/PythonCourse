sayilar = [ 1,3,5,7,9,12,19,21]

#SAyılar listesini while döngüsü ile ekrana yazdır
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1
    
#ºBaşlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
bas = int(input('baslangic :'))
bitis = int(input('bitis :'))
i=bas
while i < bitis:
    i+=1
    if i%2==0:
        print(i)
    
# 1-100 arasındaki sayıları azalan şekilde yazdırın
i =100
while i>0:
    print(i)
    i-=1

#Kullanıcıdan alacağpınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
numbers = []
i=0
while i<5:
    sayi=int(input('sayi='))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
#Kullanıcıdan alacağınız sınırsız ürünb bilgisini urunler listes
urunler =[]
adet = int(input('kaç ürün eklemek istiyorsunuz:'))
i=0

while(i<adet):
    name = input('ürün ismi :')
    price = input('ürün fiyati :')
    urunler.append({
        'name':name,
        'price':price
        })
    i+=1
for urun in urunler:
    print(f'ürün adi : {urun["name"]} ve ürün fiyati : {urun["price"]}')