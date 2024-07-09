import math

print("Hesap Makinesi")
sayi_has = 0
sayi1 = input(" sayı giriniz")
while sayi_has != 1:

    islem = input("Yapılacak işlemi giriniz(+ - * /)")
    sayi2 = input("sayı giriniz")

    if islem == '+':
        sayi1 = int(sayi1)+int(sayi2)
        print("Cevap: " + str(sayi1))

    elif islem == '-':
        sayi1 = int(sayi1)-int(sayi2)
        print("Cevap: " + str(sayi1))
    elif islem == '*':
        sayi1 = int(sayi1) * int(sayi2)
        print("Cevap: " + str(sayi1))

    elif islem == '/':
        sayi1 = int(sayi1) / int(sayi2)
        print("Cevap: " + str(sayi1))


    else:
        print("Geçersiz Giriş")
