import string
from itertools import product

def vigenere_sifre_coz(sifreli_metin, anahtar):
    anahtar = anahtar.lower()
    cozulmus_metin = ""
    anahtar_uzunlugu = len(anahtar)
    anahtar_index = 0

    for char in sifreli_metin:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            kaydirma = ord(anahtar[anahtar_index % anahtar_uzunlugu]) - ord('a')
            cozulmus_char = chr((ord(char) - base - kaydirma) % 26 + base)
            cozulmus_metin += cozulmus_char
            
            anahtar_index += 1
        else:
            cozulmus_metin += char

    return cozulmus_metin

def anahtar_kombinasyonlarini_deneyin(sifreli_metin, dosya_adi):
    alfabe = string.ascii_lowercase
    with open(dosya_adi, 'w') as dosya:
        for uzunluk in range(1, 27):  # 1'den 26'ya kadar
            for anahtar in product(alfabe, repeat=uzunluk):
                anahtar_str = ''.join(anahtar)
                cozulmus_metin = vigenere_sifre_coz(sifreli_metin, anahtar_str)
                dosya.write(f"Anahtar: {anahtar_str} => Çözülmüş Metin: {cozulmus_metin}\n")

# Şifreli metin
sifreli_metin = "xkzmiugtrxdyaqvljhvk"
dosya_adi = "vigenere_sifre_cozumu.txt"

# Anahtar kombinasyonlarını dene ve sonuçları dosyaya kaydet
anahtar_kombinasyonlarini_deneyin(sifreli_metin, dosya_adi)

print(f"Tüm çözümler '{dosya_adi}' dosyasına kaydedildi.")
