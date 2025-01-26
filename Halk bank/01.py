hasap = 0

username = input("Username: ")
password = input("password: ")

if username == "sohbet":
    if password == "12345678":
        print("hos geldiniz")
        while True:
            secim=int(input('''
1-nagt goýmak
2-nagt çekmek
3-balansy barlamak
4-basga birine pul oklamak
5-çykmak
    '''))
            if secim == 1:
                muktar = int(input("goýuljak mukdary giriziň:"))
                hasap += muktar
                print("ynnanlyk balansyňyz:", hasap, "TMT")
            elif secim == 2:
                muktar = int(input("çekiljek mukdary giriziň: "))
                if muktar > hasap:
                    print("kämil däl balans! ynnanlyk balansyňyz:", hasap, "TMT")
                else:
                    hasap -= muktar  
                    print("ynnanlyk balansyňyz", hasap, "TMT")
            elif secim == 3:
                guncelhasap = hasap 
                print("ynnanlyk balansyňyz:", guncelhasap, "TMT")
            elif secim == 4:
                kisi = input("kime oklamaly adamyň ady we familiýasy:")
                muktar = int(input("transfert ediljek mukdary giriziň"))
                if muktar > hasap:
                    print("kämil däl balans")
                else:
                    print(kisi + " atly adama ", muktar, "TMT", "transfer edildi!")
                    hasap -= muktar
                    print("ynnanlyk balansyňyz:", hasap, "TMT")
            elif secim == 5:
                print("Bizi saýlanlygyňyz üçin minnetdarlyk bildirýäris, gowy günler!")

    else:
        print("yalnys tazeden barlap gorun!")
else:
    print("yalnys tazeden barlap gorun!")
