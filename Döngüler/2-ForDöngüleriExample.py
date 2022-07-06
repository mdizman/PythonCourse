sayilar = [1,3,5,7,9,12,18,21]
#SAyilar listesişndeki hangi sayilar 3 ün katıdır
for sayi in sayilar:
   if (sayi %3 ==0):
       print(sayi)

# SAyilar listesindeki sayiların toplamı nedir
toplam = 0
for sayi in sayilar:
    toplam = toplam+sayi

#SAyilar listesindeki tek sayiların karesini alınız
for sayi in sayilar:
    if sayi%2 == 1:
        print(sayi**2)

# ŞEhirlerden hangileri en az 5 karakterlidir
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for sehir in sehirler:
    if (len(sehir)<5):
        print(sehir)

urunler = [
    {'name: ':'samsung s6','price': '3000'},
    {'name: ':'samsung s7','price': '4000'},
    {'name: ':'samsung s8','price': '5000'},
    {'name: ':'samsung s9','price': '6000'},
    {'name: ':'samsung s10','price': '7000'},
    ]
# urunlerin fiyatları toplamı nedir
toplam =0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)

# Urun fiyatı en fazla 5000 olanları getir
for urun in urunler:
   if (int(urun['price'])<=5000):
       print(urun['name'])
    
    