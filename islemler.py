import random

def yeni_kullanici():
    cikis = "z"
    with open('dosya.txt', 'r') as uzunluk:  #with dosyanın otomatik oolarak kapanmasını sağlar
        indeks = len(uzunluk.readlines())#indeks kaçıncı satır olduğunu tutuyo id yerine yazıyoruz
        indeks=indeks-1
    while cikis != "h" or "H" :

        ad = str(input("Lütfen adınızı giriniz"))
        soyad = str(input("Lütfen soyadınızı giriniz"))
        dogum_tarihi = str(input("Lütfen doğum tarihinizi giriniz (sayılar arasına nokta koyunuz)"))
        dogum_yeri = str(input("Lütfen doğum yerinizi giriniz"))

        try :
            dosya = open("dosya.txt", "a")    #dosyayı yazmak için açar dosya yoksa oluşturur içeriğine dokunmaz
            dosya.write("{},{},{},{},{}".format(indeks,ad,soyad,dogum_tarihi,dogum_yeri,))
            dosya.write("\n")
            indeks = indeks+1
        except (ValueError):
            print("hatalı karakter girdiniz")

        cikis = input("çıkmak için h'ye devam etmek için herhangi bir tuşa basınız")
        if cikis == "h" or cikis == "H":
            break

#hata çıkarabilecek kod parçası try ın içine yazılır,hata durumund yapılacaklar except içine yazılır


def kullanici_getir():
    cikis = "z"
    satir_sayisi= int(0)

    while cikis != "h" or "H" :

        with open('dosya.txt', 'r') as dosya:
            for satir in dosya:
                satir_sayisi += 1

        id = int(input("lütfen id giriniz"))

        if satir_sayisi < id:
            print("hatalı id girişi")  #kayıtlı olmayan id girildiğinde hata mesajı bastırır

        else :
            dosya = open("dosya.txt", "r") #dosyayı okumak için açar
            a = dosya.readlines()[id].replace("\t","")  #dosya içeriğini a ya atar
            print(a)


        cikis = input("çıkmak için h'ye devam etmek için herhangi bir tuşa basınız")
        if cikis == "h" or cikis == "H":
            break



def kullaniciAdi_sifre_uret ():


    try:
        with open('dosya.txt', 'r+') as dosya:    #with dosyanın otomatik olarak kapanmasını sağlar
            karakterler = ["*", " /", "!", "_", "(", ")", "&", "%", "+", "-", ".", ",", "<", ">"]
            icerik = dosya.readlines()

            for i in range(1, len(icerik)):
                rastgele = random.choice(karakterler) #karakterler listesi içinden rastgele karakter seçtiğimiz satır
                ekrana = icerik[i].lower().replace("\t","")  #  küçük harfe dönüştür boşluk sil

                liste = ekrana.split(",")[:] #her virgüldeki değeri listenin bir elemanı olarak atıyo

                ad = liste[1]    #liste[0] id yi veriyor
                #ad = list(ad)
                harf2 = ad[1]
                harf4 = ad[3]
                adim1 = harf2+harf4

                soyad = liste[2]
                ilkharf = soyad[0]
                son3harf = soyad[-3:]
                ortaharf = son3harf[1]
                adim2 = son3harf.replace(ortaharf,ilkharf)

                tarih = liste[3]
                tarih = tarih.replace("-","")
                toplam = tarih[2]+tarih[3]+tarih[4]+tarih[5]+tarih[6]+tarih[7]
                yilson2 = tarih[6:]
                adim3 = toplam+yilson2

                kullaniciadi = adim2 + adim1 + adim3

                ad = liste[1]
                a = ad[0]
                b = ad[-1].upper()
                islem1 = a+b
                islem1 = str(islem1)
                soyad = liste[2]
                son2 = soyad[-2:-1]
                son1 = soyad[-1]
                son1 = rastgele
                islem2 = son2 + son1
                islem2=str(islem2)

                tarih = liste[3]
                tarih = tarih.replace("-","")
                son22 = tarih[-2: ]
                ay = int(tarih[2:4])
                aykare = ay*ay
                aykare = str(aykare)
                islem3 = son22+aykare
                islem3=str(islem3)

                dogumyeri = liste[4]
                yer = dogumyeri[1:-1]
                yer = yer[0].upper() + yer[1:-1] + yer[-1].upper()
                islem4 = yer
                islem4=str(islem4)

                islem5 = random.randint(10, 99)
                islem5=str(islem5)

                sifre = islem4+islem5+islem1+islem3+islem2



                metin = open("kullaniciAdi_sifre.txt", "a") #dosyayı yazmak için açan satır
                metin.write(kullaniciadi + "     " + sifre)
                metin.write("\n")



    except (ValueError):
            print("hatalı karakter girdiniz")





def anlik_uret ():

    karakterler = ["*"," /", "!","_","(",")","&","%","+","-",".",",","<",">"]
    indeks = random.randint(0, len(karakterler) - 1)
    rastgele = karakterler[indeks]

    #kullanıcıdan veri girişinin alındığı satırlar
    id = input("lütfen id giriniz")
    ad = input("lütfen adınızı giriniz")
    soyad = input("lütfen soyadınızı giriniz")
    dogumyeri = input("lütfen doğum yeri giriniz")
    tarih = input("lütfen doğum tarihinizi boşuk bırakmadan gün ay yıl olarak giriniz ör:06032001")

    harf2 = ad[1]
    harf4 = ad[3]
    adim1 = harf2+harf4

    ilkharf = soyad[0]
    son3harf = soyad[-3:]
    ortaharf = son3harf[1]
    adim2 = son3harf.replace(ortaharf,ilkharf)

    tarih = tarih.replace("-","")
    toplam = tarih[2]+tarih[3]+tarih[4]+tarih[5]+tarih[6]+tarih[7]
    yilson2 = tarih[6:]
    adim3 = toplam+yilson2

    kullaniciadi = adim2 + adim1 + adim3
    print("kullanici adınız",kullaniciadi)

    ad = list(ad)
    ad[-1] = ad[-1].upper
    ad = str(ad)
    islem1 = ad[0] + ad[-1]
    islem1 = str(islem1)

    son2 = soyad[-2:-1]
    son1 = soyad[-1]
    son1 = rastgele
    islem2 = son2 + son1
    islem2 = str(islem2)

    son22 = tarih[-2: ]
    ay = int(tarih[2:4])
    aykare = ay*ay
    aykare = str(aykare)
    islem3 = son22+aykare
    islem3 = str(islem3)

    yer = dogumyeri[1:-1]
    yer = yer[0].upper() + yer[1:-1] + yer[-1].upper()
    islem4 = yer
    islem4 = str(islem4)

    islem5 = random.randint(10, 99)
    islem5 = str(islem5)

    sifre = islem4+islem5+islem1+islem3+islem2

    print("şifreniz",sifre)

    #bu satı bu koda sonradan eklenmiştir.
