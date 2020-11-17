sayi1=int(input("Sayı girin: "))
sayi2=int(input("Sayı girin: "))
sayi3=int(input("Sayı girin: "))
sayi4=int(input("Sayı girin: "))

dizi=[]

if sayi1<10 and sayi2<10 and sayi3<10 and sayi4<10:
    sonuc=sayi1*sayi2*sayi3*sayi4
    dizi.append(sonuc)
    

elif sayi1>10 and sayi2>10 and sayi3>10 and sayi4>10:
    sonuc=sayi1+sayi2+sayi3+sayi4
    dizi.append(sonuc)
    

print(dizi)


    
