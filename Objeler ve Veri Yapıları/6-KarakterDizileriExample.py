mail="mehmetdizman29@gmail.com"
konu="Bu ders serisinde Python Programlama dilini temelden iyi derecede öğreniyoruz."

# Konu dizisinde kaç karakter bulunmakta
result=len(konu)
print(result)

length=len(mail)
length2=len(konu)

# Mail dizisinden @ karkaterini alalım
result2=mail[14:15]
print(result2)

# Mail dizisinden com karkaterini alalım
result3=mail[length-3:length]
print(result3)

# Konu dizisinden ilk 15 ve son 15 karkateri alalım
x= konu[0:15]
y=konu[:15]
z=konu[-15:]
print(x)

# Konu dizisi tersten yazdıralım
ters=konu[::-1]
print(ters)

# Verilen ifadelerle düzgün bir cümle yazdıralım
    # " Benim adım Mehmet Dizman , Yaşım 22 ve mesleğim mühendis. " 
name,surname,age,job = 'Mehmet','Dizman',22,'mühendis'
print(f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}")

# Hello world ifadesindeki w rarfini 'W' ile değiştirelim
s='Hello world'
s=s[0:6] + 'W' + s[-4:]
print(s)

#abc ifadesini yanyana 3 kere yazdıralım
abc='abc'*3
print(abc)