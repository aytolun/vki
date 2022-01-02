#4.soru
#vücut kitle indexini fonksiyon ile hesapıyoruz

def vki (boy,kilo):

    return kilo / (boy*boy)*10000

def main():
    #bu fonksiyon içinde gerekli bilgileri alıyoruz ve yazdırıyoruz
   
    boy=int(input("boyunuzu cm cinsinden giriniz: "))
    kilo=int(input("kilonuzu kg cinsinden giriniz: "))
    hesapla=int(vki(boy,kilo))
    print(hesapla)
    if hesapla<18:
        print("ZAYIF")
    elif 18 <= hesapla <= 24:
        print("NORMAL")
    elif 25 <= hesapla <= 29:
        print("FAZLA KİLO")
    elif 30 <= hesapla <= 39:
        print("OBEZ")
    elif 40 <= hesapla:
        print("MORBİD OBEZ")
    else:
        ("yanlıs girdiniz.")
    

main() #burada fonksiyonu cagırıyoruz
