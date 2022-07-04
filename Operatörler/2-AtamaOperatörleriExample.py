x,y,z=2,5,10

numbers=1,5,7,10,6

# Kulanıcıdan alınan 2 sayının çarpımını x y z toplamının farklı nedir

a = int(input('sayi1:'))
b = int(input('sayi2:'))

result= (a*b) - (x+y+z)
print(result)

# y nin x e kalansız bölümünü hesapla
result=y//x

# x y z toplamının mod 3 ü nedir
result = (x+y+z)%3

# y nin x inci kuvveti
result = y**x

# x *y z = numbers işlemine göre z nin küpü kaçtır
numbers =1,5,7,10,6
x,*y,z=numbers
result = z**3

