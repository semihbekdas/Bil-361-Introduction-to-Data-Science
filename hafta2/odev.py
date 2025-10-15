"""Hafta 2 ödevleri için yardımcı fonksiyonlar."""
from __future__ import annotations

import math
import random
from typing import Iterable, List, Sequence, Tuple


def metni_goster(metin: str) -> str:
    """Kullanıcının girdiği metni geri döndür."""
    return metin


def iki_sayi_topla(birinci: float, ikinci: float) -> float:
    """İki sayısal değerin toplamını hesapla."""
    return birinci + ikinci


def cift_mi(sayi: int) -> bool:
    """Sayı çift ise True, tek ise False döndür."""
    return sayi % 2 == 0


def basit_islem(birinci: float, ikinci: float, operator: str) -> float:
    """İki sayı arasında temel aritmetik işlemi gerçekleştir."""
    if operator == "+":
        return birinci + ikinci
    if operator == "-":
        return birinci - ikinci
    if operator == "*":
        return birinci * ikinci
    if operator == "/":
        if ikinci == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılmaz.")
        return birinci / ikinci
    raise ValueError(f"Desteklenmeyen operatör: {operator}")


def guvenli_hesapla(birinci: float, ikinci: float, operator: str) -> Tuple[bool, float | None]:
    """Kullanıcı hatalarını engellemek için hesaplamayı güvenli şekilde yürüt."""
    try:
        return True, basit_islem(birinci, ikinci, operator)
    except (ZeroDivisionError, ValueError):
        return False, None


def toggleda_ayarla(baslangic_degeri: int, tus_sayisi: int) -> int:
    """Her seferinde artıp azalarak değeri birer birer güncelle."""
    deger = baslangic_degeri
    for sira in range(tus_sayisi):
        deger += 1 if sira % 2 == 0 else -1
    return deger


def ondan_eksi_ona() -> List[int]:
    """10'dan başlayıp -10'a kadar tüm sayıları listele."""
    return list(range(10, -11, -1))


def harfleri_virgulle(metin: str) -> str:
    """Verilen metindeki her karakter arasına virgül yerleştir."""
    return ",".join(metin)


def rastgele_tamsayilar(adet: int = 10, baslangic: int = 1, bitis: int = 100) -> List[int]:
    """Belirtilen aralıkta rastgele tam sayılar üret."""
    if adet <= 0:
        return []
    return [random.randint(baslangic, bitis) for _ in range(adet)]


def bese_bolunenler(baslangic: int = -100, bitis: int = 100) -> List[int]:
    """Belirtilen aralıktaki 5'e tam bölünen sayıları döndür."""
    return [sayi for sayi in range(baslangic, bitis + 1) if sayi % 5 == 0]


def uc_sayiyi_sirala(birinci: float, ikinci: float, ucuncu: float) -> List[float]:
    """Üç sayıyı küçükten büyüğe sırala."""
    return sorted([birinci, ikinci, ucuncu])


def faktoriyel_acilimi(sayi: int) -> Tuple[int, str]:
    """Faktöriyeli hesapla ve açılım metnini döndür."""
    if sayi < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if sayi in (0, 1):
        return 1, f"{sayi}! = 1"
    carpanlar = list(range(sayi, 0, -1))
    sonuc = math.prod(carpanlar)
    acilim = " * ".join(str(deger) for deger in carpanlar)
    return sonuc, f"{sayi}! = {acilim} = {sonuc}"


def ilk_ve_son_kelime(metin: str) -> Tuple[str | None, str | None]:
    """Cümlenin ilk ve son kelimesini döndür."""
    kelimeler = metin.split()
    if not kelimeler:
        return None, None
    return kelimeler[0], kelimeler[-1]


def toplam_ve_ortalama(sayilar: Iterable[float]) -> Tuple[float, float | None]:
    """Değerlerin toplamını ve aritmetik ortalamasını hesapla."""
    liste = list(sayilar)
    if not liste:
        return 0.0, None
    toplam = sum(liste)
    return toplam, toplam / len(liste)


def harfleri_degistir(metin: str) -> str:
    """Küçük harfleri büyüğe, büyük harfleri küçüğe çevir."""
    return metin.swapcase()


def zam_uygula(maas: float, yuzde_artis: float) -> float:
    """Yüzdesel zam sonrası yeni maaşı hesapla."""
    return maas * (1 + yuzde_artis / 100)


def rakamlar_toplami(sayi: int) -> int:
    """Tam sayının rakamlarının mutlak toplamını döndür."""
    return sum(int(rakam) for rakam in str(abs(sayi)))


def tek_cift_ekle(sayilar: Iterable[int]) -> List[str]:
    """Girilen her sayının yanına tek/çift bilgisini ekle."""
    etiketli: List[str] = []
    for deger in sayilar:
        durum = "even" if cift_mi(deger) else "odd"
        etiketli.append(f"{deger} {durum}")
    return etiketli


def on_bire_bolunenler(baslangic: int = 1, bitis: int = 300) -> List[int]:
    """Belirtilen aralıktaki 11'e tam bölünen sayıları döndür."""
    return [sayi for sayi in range(baslangic, bitis + 1) if sayi % 11 == 0]


def gecis_final_notu(
    vize_notu: float,
    gecme_esigi: float = 60.0,
    vize_agirligi: float = 0.4,
    final_agirligi: float = 0.6,
) -> float:
    """Ağırlıklı değerlendirmede dersi geçmek için gereken final notunu hesapla."""
    kalan = gecme_esigi - vize_notu * vize_agirligi
    if final_agirligi <= 0:
        raise ValueError("Final weight must be positive.")
    return max(0.0, kalan / final_agirligi)


def ucgen_alani(kenar_a: float, kenar_b: float, kenar_c: float) -> float:
    """Heron formülü ile üçgenin alanını hesapla."""
    if kenar_a <= 0 or kenar_b <= 0 or kenar_c <= 0:
        raise ValueError("Triangle sides must be positive.")
    if (
        kenar_a + kenar_b <= kenar_c
        or kenar_a + kenar_c <= kenar_b
        or kenar_b + kenar_c <= kenar_a
    ):
        raise ValueError("Provided sides do not form a triangle.")
    yari_cevre = (kenar_a + kenar_b + kenar_c) / 2
    return math.sqrt(
        yari_cevre
        * (yari_cevre - kenar_a)
        * (yari_cevre - kenar_b)
        * (yari_cevre - kenar_c)
    )


SESLI_HARFLER = set("aeiouAEIOUıİöÖüÜ")


def sesli_harf_say(metin: str) -> int:
    """Metindeki sesli harf sayısını bul."""
    return sum(1 for karakter in metin if karakter in SESLI_HARFLER)


def sayilari_satirda_tekrar_et(sayilar: Sequence[int]) -> List[str]:
    """Her sayıyı mutlak değeri kadar yan yana yazarak döndür."""
    satirlar: List[str] = []
    for sayi in sayilar:
        tekrar = abs(sayi)
        satirlar.append(str(sayi) * tekrar if tekrar else "")
    return satirlar


def tekrarsiz_rastgele_sayilar(adet: int, baslangic: int, bitis: int) -> List[int]:
    """Belirtilen aralıkta tekrarsız rastgele tam sayılar üret."""
    aralik = bitis - baslangic + 1
    if adet > aralik:
        raise ValueError("Count exceeds the number of available unique values.")
    if adet <= 0:
        return []
    return random.sample(range(baslangic, bitis + 1), adet)


def asal_carpanlari(sayi: int) -> List[int]:
    """Bir tam sayının asal çarpanlarını döndür."""
    if sayi == 0:
        raise ValueError("Zero does not have defined prime factors.")
    carpanlar: List[int] = []
    hedef = abs(sayi)
    bolen = 2
    while bolen * bolen <= hedef:
        while hedef % bolen == 0:
            carpanlar.append(bolen)
            hedef //= bolen
        bolen += 1 if bolen == 2 else 2
    if hedef > 1:
        carpanlar.append(hedef)
    if sayi < 0:
        carpanlar[0:0] = [-1]
    return carpanlar


def en_uzun_kelime(metin: str) -> str | None:
    """Metindeki en uzun kelimeyi bul."""
    kelimeler = metin.split()
    if not kelimeler:
        return None
    return max(kelimeler, key=len)


def harf_notunu_bul(not_degeri: float) -> str:
    """Sayısal notu harf notuna çevir."""
    if not_degeri >= 90:
        return "A"
    if not_degeri >= 80:
        return "B"
    if not_degeri >= 70:
        return "C"
    if not_degeri >= 60:
        return "D"
    return "F"


def kelimeleri_ters_cevir(cumle: str) -> str:
    """Kelime sırasını koruyarak her kelimeyi tersten yaz."""
    return " ".join(kelime[::-1] for kelime in cumle.split())


MORSE_KODLARI = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    " ": "/",
}


def metni_morse_cevir(metin: str) -> str:
    """Metni Mors alfabesi koduna dönüştür."""
    kodlar = []
    for karakter in metin.upper():
        kodlar.append(MORSE_KODLARI.get(karakter, ""))
    return " ".join(filter(None, kodlar))


def kumulatif_toplam(sayilar: Iterable[float]) -> List[float]:
    """Verilen dizinin kümülatif toplamlarını üret."""
    toplamlar: List[float] = []
    biriken = 0.0
    for deger in sayilar:
        biriken += deger
        toplamlar.append(biriken)
    return toplamlar


if __name__ == "__main__":
    print("Modül, hafta 2 ödevleri için yardımcı fonksiyonlar içerir.")
