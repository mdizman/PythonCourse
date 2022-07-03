mail = "mehmetdizman29@‼gmail.com"
konu = "Bu derslerimizde python programlama dilinin temelini öğreniyoruz."

# 'Hello World' karakter dizisinin bnaşran ve sodnan silin
result = 'Hello World'.strip()
result = 'Hello World'.lstrip()
result = 'Hello World'.rstrip()

# mehmetdizman29@‼gmail.com içideki mehmetdizman bilgisi haricindeki her karakteri silin
'mehmetdizman29@‼gmail.com'.strip('29@gmail.com')

#konu içindeki her karakteri küçült
result=konu.lower()
result=konu.upper()
result=konu.title()

#mail içinde kaç tane a var
result = mail.count('a')

#mail m ile başlayıp m ile bitiyor mu
result = mail.startswith('m')
result = mail.endswith('m')

# mail içinde .com var mı
result = mail.find('.com')

# konu içindeki karakterlerin hepsi alfabetik mi 
result= konu.isalpha()
result = konu.isdigit()

# konu içindeki tüm boşluk karakterlerini - ile değiştir
result= konu.replace('', '-')

# konu içersinindeki boşluk karakterlerinden karakteri ayır
result = konu.split(' ')

print(result)