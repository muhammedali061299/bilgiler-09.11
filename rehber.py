def rehber_ekle(): 
    dosya = open("rehber.txt","a")
    print("\n\n Rebere eklenecek bilgileri giriniz:")
    ad  = input("Ad  : ")
    tel = input("Tel : ")
    dosya.write(f"{ad}#{tel}\n")
    dosya.close()
    print("\n\nRehberdekiler (yeni şekli):")
    rehber_listele()

def rehber_listele(): 
    print("\n\nRehberiniz:")
    try:
        dosya = open("rehber.txt")
    except:
        print("Dosya bulunamadı.")
        input()
    okunan = dosya.readlines()
    # print(okunan)
    # for a in okunan:
    for sira,a in enumerate(okunan):
        b = a.split("#")
        # print(b[0],"\tTelefonu:",b[1])
        # print(sira+1," - ",b[0],"\t Telefonu: ",b[1])
        print(f"{sira+1} - {b[0]},\t Telefonu: {b[1]}")
    dosya.close()

def rehber_sil(): 
    print("Mevcut kayıtlar")
    rehber_listele()
    silinecek = int(input ("Hangi kayıt silinecek(numarasını girin):"))
    dosya = open("rehber.txt","r+")    
    okunan = dosya.readlines()
    silinecekKayit = okunan[silinecek-1]
    print("Silinecek kayıt : ", silinecekKayit)
    dosya.close()

    dosya = open("rehber.txt","w")    
    for a in okunan:
        if a != silinecekKayit: dosya.write(a)
    dosya.close()
    # # print(okunan)
    # for s,a in enumerate(okunan):
    #     print(s, a)
    # dosya.close()

    # dosya = open("rehber.txt","w")
    # for s,a in enumerate(okunan):
    #     if s != silinecek: dosya.write(a)
    # dosya.close()

    # dosya = open("rehber.txt")
    # okunan = dosya.readlines()
    # print(okunan)
    # for s,a in enumerate(okunan):
    #     print(s, a)


    # dosya.close()
    # dosya = open("rehber.txt","w")

    # for sira, a in enumerate(okunan):
    #     if sira != silinecek: dosya.write(a)
    
    # dosya.close()
    

def rehber_duzelt(): 
    print("Mevcut kayıtlar")
    rehber_listele()
    duzeltilecek = int(input ("Hangi kayıt duzeltilecek(numarasını girin):"))
    dosya = open("rehber.txt","r+")    
    okunan = dosya.readlines()
    duzeltilecekKayit = okunan[duzeltilecek-1]
    print("Düzeltilecek kayıt : ", duzeltilecekKayit)
    dosya.close()

    dosya = open("rehber.txt","w")    
    for a in okunan:
        if a == duzeltilecekKayit: 
            print("\n\n Yeni bilgileri giriniz:")
            ad  = input("Ad  : ")
            tel = input("Tel : ")
            dosya.write(f"{ad}#{tel}\n")
        else: dosya.write(a)

    dosya.close()

def anamenu():
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    print("╔═══════════════════╗") # ╠ ╬ 
    print("║ REHBER UYGULAMASI ║")    
    print("╠═══════════════════╣")
    print("║ 1-Rehbere ekle    ║")
    print("║ 2-Kişi listesi    ║")
    print("║ 3-Kişi düzenle    ║")
    print("║ 4-Kişi silme      ║")
    print("║ 5-Çıkış           ║")
    print("║ Seçiniz nedir?    ║")
    print("╚═══════════════════╝")
    secim = input()
    if secim == "1" : rehber_ekle(); anamenu()   
    if secim == "2" : rehber_listele(); anamenu()
    if secim == "3" : rehber_duzelt(); anamenu()
    if secim == "4" : rehber_sil(); anamenu()
    if secim == "5" : rehber_ekle(); anamenu()
    
anamenu()