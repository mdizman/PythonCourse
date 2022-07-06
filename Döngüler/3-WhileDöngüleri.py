# 1 den 100 e kadar yazdır
x=0
while x<=100:
    print(x)
    x=x+1
print('Bitti...')

x=1
while x<=100:
    if (x %2 ==0):
        print(x)
    x=x+1
    
print('Bitti...')


x=1
while x<=100:
    if (x %2 ==1):
        print(f'sayi tek :{}')
    else:
        print(f'sati cift:{}')
    x+=1
    
print('Bitti...')