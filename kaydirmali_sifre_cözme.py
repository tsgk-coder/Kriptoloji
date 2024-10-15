def kaydirma_sifre_coz(sifreli_metin, kaydirma):
    cozulmus_metin = ""
    
    for char in sifreli_metin:
        if char.isalpha():  # Harfleri kontrol et
            # Harfin ASCII değerini al ve kaydır
            base = ord('a') if char.islower() else ord('A')
            cozulmus_char = chr((ord(char) - base - kaydirma) % 26 + base)
            cozulmus_metin += cozulmus_char
        else:
            cozulmus_metin += char  # Harf değilse olduğu gibi ekle

    return cozulmus_metin

sifreli_metinler = [
    "exvliuhohphbrqwhplklfdpdklfjxyhqolghjlo", # kaydırma miktarı: 3 busifrelemeyontemihicamahicguvenlidegil
    "fnlmtytdxftetmtmnkd",                      # kaydırma miktarı: 19 mustafakemalataturk
    "qaxizbicgoctiuitqjqtqutmzcvqdmzaqbmaq",    # kaydırma miktarı: 8 ispartauygulamalıbilimler
    "ehvlnwdvmlpqdvwlnnxoxex",                  # kaydırma miktarı: 3 besiktasjimnastikkulubu
    "mewrebsiodiejikcsxnk"                      # kaydırma miktarı: 10 cumhuriyetyuzyasinda
]

# Örnek kaydırma miktarı (5) ile çözümleme
kaydirma_miktari = 19
for metin in sifreli_metinler:
    print(kaydirma_sifre_coz(metin, kaydirma_miktari))
