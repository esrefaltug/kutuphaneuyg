import os
kitapListe=list()

menu="""
[1]Kitap Ekle
[2]Kitap Al
[3]Tümünü Listele
[Q]Çıkış

"""

def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı")
    print("Ana menüye dönmek için enter'e basın.")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
    
def kitapCıkar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        #kitap çıkartılıyor
        liste.remove(kitap)
        print("kitap çıkartma işlemi tamamlandı")
        print("Ana menüye dönmek için enter'e basın.")
        input()

    else:
        print("Arattığınz kitap mevcut değildir.")
        print("Ana menüye dönmek için enter'e basınız.")
        input()
def Listele(liste:list):
    for i in liste:
        print("Kitap Adı: {}-----> Yazar:{}".format(i[0],i[1]))
    print("Ana menüye dönmek için enter'e basın.")
    input()
        


    
while True:
    os.system("cls")#terminal ekranını temizler.
    print(menu)

    secim=input("işleminizi seçiniz.")

    if secim=="1":
        kitap_isim=input("Kitabın adı: ")
        kitap_yazar=input("yazarın adı: ")
        kitap=(kitap_isim,kitap_yazar)
        kitapEkle(kitap,kitapListe)
        
        
    elif secim=="2":
        kitap_isim=input("Kitabın adı: ")
        kitap_yazar=input("Yazarın adı: ")
        kitap(kitap_isim,kitap_yazar)
        kitapCıkar(kitap,kitapListe)

 
    
    elif secim=="3":
        pass
    elif secim=="Q" or secim=="q":
        quit()

    else:
        print("Hatalı giriş yaptınız...")

        
        
