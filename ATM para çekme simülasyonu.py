#CÜZDAN SİMÜLASYONU
mevcut_para =1000
while True:

    print("1-bakiye sorgula")
    print("2-para çek")
    print("3-para yatır")
    print("4-çıkış")
    secim = input("bir seçenek girin.")

    if secim == "1":
        print(f"bakiye sorgulanıyor...\nMevcut bakiye = {mevcut_para} TL")
        
    elif secim == "2":
        cekim_miktari = input("çekmek istediğiniz para miktarını girin: ")
        print(f"çekilen tutar: {cekim_miktari}")
    elif secim == "3":
        yatan_para = int(input("bankaya yatırmak  para miktarını girin: "))
        print(f"yatırılan para miktarı: {yatan_para}")
    elif secim == "4":
        print("çıkış yapılıyo...")
        break


    
    



        
    




    
