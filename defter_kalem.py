defter = int(input("kaç adet defter aldınız : "))

defter_fiyat = 40

defterler_fiyat = defter * defter_fiyat

kalem= int(input("kaç adet kalem aldınız : "))

kalem_fiyat = 20

kalemler_fiyat = kalem * kalem_fiyat

toplam_fiyat = defterler_fiyat + kalemler_fiyat

print("toplam fiyat ", toplam_fiyat, "TL dir")

indirim = toplam_fiyat * 15 / 100

indirimli_fiyat = toplam_fiyat - indirim

print("İndirimli fiyat:", indirimli_fiyat, "TL'dir")