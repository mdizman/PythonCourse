#Kullanıcıdan isim yaş ve eğtim bilgileribi isteyip ehliyet alabilme durumunu kontrol ediniz
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input('isim giriniz :')
yas = int(input('yas :'))
egitim = input('Eğitim giriniz :')


if yas > 18 and egitim==['Lise', 'Üniversite']:
    print('Ehliyet almya uygun')
else:
    print('Ehliyet alamaz')
    
# Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#not aralığını karşılık gelen not bilgisine göre yazdırınız
# 0-24 = 0
# 25-44 =1
# 45-54 =2
# 55-69 = 3
# 70-84 =4
# 85- 100 = 5

yazili1 = int(input('Birinci yazılı :'))
yazili2 = int(input('İkinci yazılı :'))
ortalama = (yazili1+yazili2)/2
if (0<ortalama<24):
    print('Harf notu 0')
elif (25<ortalama<44):
    print('Harf notu 1')
elif (45<ortalama<54):
    print('Harf notu 2')
elif (55<ortalama<69):
    print('Harf notu 3')
elif (70<ortalama<84):
    print('Harf notu 4')
elif (85<ortalama<100):
    print('Harf notu 5')
    
    
#Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilerde verilmiştir
#1. Bakım = 1. yıl
#2. Bakım = 2. yıl
# 3. Bakıkm = 3.yıl
# Süre hesabını alınan gün ay yılk bilgisine göre gün bazlı hesaplayınız 
# datetime methodu kullanmamız gerekiyor
# (simdi) - (2018/8/1) = gün

import datetime
tarih = input('aracınız hangi tarihte trafiğe çıkmıştır:')
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi -trafigeCikis
days =(fark.days)
if (days <= 365):
    print('1. servis aralığı')
elif (days > 365 and days <=365*2):
    print('2. servis aralığı')
elif (days > 365*2 and days <=365*3):
    print('3. servis aralığı')
else:
    print('hatalı süre.')






