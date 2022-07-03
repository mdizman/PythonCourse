numbers = [1 ,15,2,6,7,52,9]
letters = ['a','c','f','y','b']

val = min (numbers)
val = max (numbers)
val = min (letters)
val = max (letters)

val = numbers[3:6]

numbers[4]=40

numbers.append(49) # Sona ekleme
numbers.insert(3, 78) #3. index den önce 78 ekle
numbers.insert(-1,4) # sona ekleme

numbers.pop() # sondan sil
numbers.pop(0) # 1. elemanı siler
numbers.remove(49) # silmek istenilen karakter belirlenir ve silinir

numbers.sort() # Liste sayısal olarak sıralanır 
letters.sort() # alfabetik olarak

print(len(numbers))


print(val)