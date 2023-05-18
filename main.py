import islemler

def main():
      secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz \n 1.Yeni kullanıcı bilgileri girme \n "
      "2.Kayıtlı kullanıcı bilgilerini ekrana yazdırma \n 3.Dosyadaki bilgilerden kullanıcı adı-güçlü şifre üret \n "
      "4.Anlık girdiyle kullanıcı adı-güçlü şifre üret"))

      if secim == 1:
            islemler.yeni_kullanici() #islemler den yeni kullanıcı fonksiyonunu çalıştırır

      elif secim == 2 :
            islemler.kullanici_getir() #islemler den kullanici getir fonksiyonunu çalıştırır

      elif secim == 3 :
            islemler.kullaniciAdi_sifre_uret() #islemler den kullaniciAdi_sifre_uret fonksiyonunu çalıştırır

      elif secim == 4 :
            islemler.anlik_uret() #islemler den anlik_uret fonksiyonunu çalıştırır

      else:
            print("hatalı giriş")



main() #main fonksiyonunu getirip çalıştırır