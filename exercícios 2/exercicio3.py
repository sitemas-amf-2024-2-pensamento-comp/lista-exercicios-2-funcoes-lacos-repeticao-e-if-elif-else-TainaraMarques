a = int(input("digite um número: "))
b = int(input("digite um número: "))
n1 = a + 1
n2 = b + 1

if a < b:
    while n1 > a and n1 < b:
        if n1 % 3 == 0:
            print (n1)
        n1 += 1

else:
    while n2 < a and n2 > b:
        if n2 % 3 == 0:
            print (n2)
        n2 += 1