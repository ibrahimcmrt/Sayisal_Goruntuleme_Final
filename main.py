from PIL import Image, ImageFilter
import os

def keskinlestir_ve_kaydet(resim_yolu, keskinlik_faktoru):
    # Resmi yükle
    resim = Image.open(resim_yolu)

    # Keskinleştirme filtresi
    keskin_resim = resim.filter(ImageFilter.UnsharpMask(radius=2, percent=keskinlik_faktoru))

    # Keskinleştirilmiş resmi masaüstüne kaydet
    masaustu_yolu = os.path.expanduser("/Users/ibrahimcomert/Desktop")  # Kullanıcının masaüstü yolu
    yeni_resim_ad = "keskinlestirilmis_resim.png"
    yeni_resim_yolu = os.path.join(masaustu_yolu, yeni_resim_ad)
    keskin_resim.save(yeni_resim_yolu)

    print(f"Keskinleştirilmiş resim başarıyla kaydedildi: {yeni_resim_yolu}")

if __name__ == "__main__":
    # Keskinleştirme faktörü
    keskinlik_faktoru = 87

    # Keskinleştirme işlemi için kullanılacak resmin dosya yolu
    resim_yolu = "/Users/ibrahimcomert/Desktop/1.png"

    # Keskinleştirme işlemini uygula ve keskinleştirilmiş resmi masaüstüne kaydet
    keskinlestir_ve_kaydet(resim_yolu, keskinlik_faktoru)
