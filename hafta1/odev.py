"""Hafta 1 ders notlarindan ornek Python kodlari."""
from __future__ import annotations

from abc import ABC, abstractmethod


# Kalitimin temel ornegi
class Animal:
    pass


class kus(Animal):
    pass


a = Animal()


# Soyut sinif kullanimi
class Animal(ABC):
    @abstractmethod
    def yurume(self) -> None:
        pass

    @abstractmethod
    def kosma(self) -> None:
        pass


class kus(Animal):
    def __init__(self) -> None:
        print("kus olusturuldu")

    def yurume(self) -> None:
        print("kuslar pek yurumez")

    def kosma(self) -> None:
        print("kuslar pek kosmazda")


# a = Animal()  # Soyut siniflardan dogrudan nesne olusturulmaz.
b = kus()
b.kosma()
b.yurume()


# Overriding ornegi
class Animal:
    def sesVer(self) -> None:
        print("ses cikarirlar")


class kedi(Animal):
    def sesVer(self) -> None:
        print("miyav")


a = Animal()
a.sesVer()

k = kedi()
k.sesVer()


# Polimorfizm ornekleri
class Hayvanlar:
    def __init__(self, isim: str) -> None:
        self.isim = isim

    def tepki(self) -> str:
        raise NotImplementedError("HATA")


class Kedi(Hayvanlar):
    def tepki(self) -> str:
        return "Miyav!"


class Kopek(Hayvanlar):
    def tepki(self) -> str:
        return "Haav! Hav!"


hayvan = [Kedi("Boncuk"), Kedi("Tekir"), Kopek("Elmas")]
for hyvn in hayvan:
    print(hyvn.isim + ": " + hyvn.tepki())


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> str:
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self) -> str:
        return "Meow!"


class Dog(Animal):
    def talk(self) -> str:
        return "Woof! Woof!"


animals = [Cat("Missy"), Cat("Mr. Mistoffelees"), Dog("Lassie")]
for animal in animals:
    print(animal.name + ": " + animal.talk())


"""Sorular:
1. Hangisi encapsulation tanimidir?
    Cevap: C - Bir nesnenin metot ve verilerini diger nesnelerden saklayarak erisimi
    engellemektir.
2. Yandaki kodla ilgili dogru bilgi hangisidir?
    Cevap: B - B sinifi A'dan miras alir.
3. Hangisi soyut sinif tanimidir?
    Cevap: B - OOP'de nesnesi olmayan siniflara verilen isimdir.
"""


class A:
    def __init__(self, a: int) -> None:
        print("a sinifi olusturuldu")
        self.a = a

    def ilk(self) -> None:
        print("ilk isimli metot")


class B(A):
    def __init__(self, j: int = 10) -> None:
        self.j = j
        super().__init__(a=j)


class Animal:
    def sesVer(self) -> None:
        print("ses cikarirlar")


class kedi(Animal):
    def sesVer(self) -> None:
        print("miyav")


a = Animal()
a.sesVer()  # cikti: ses cikarirlar

k = kedi()
k.sesVer()  # cikti: miyav


class Animal:
    def __init__(self) -> None:
        print("hayvan sinifinin yapici metotu")

    def sesCikar(self) -> None:
        print("hav,miyav,vak....")

    def hareket(self) -> None:
        print("ziplar,kosar,yurur..")


class kedi(Animal):
    def __init__(self) -> None:
        super().__init__()
        print("kedi sinifi olusturuldu")

    def sesCikar(self) -> None:
        print("miyav")

    def DokuzCan(self) -> None:
        print("Bu sevimli hayvanlar hep dort ayak ustune duser")


k1 = kedi()
k1.sesCikar()
k1.hareket()
k1.DokuzCan()


class kus(Animal):
    def __init__(self) -> None:
        print("kus sinifi olusturuldu")
        super().__init__()

    def ucma(self) -> None:
        print("kanatlari vardir ucarlar")


kus1 = kus()
kus1.ucma()
kus1.hareket()


class Banka2:
    def __init__(self, isim: str, para: int, adres: str) -> None:
        self.__isim = isim
        self.__para = para
        self.__adres = adres

    def getPara(self) -> int:
        return self.__para

    def setPara(self, miktar: int) -> None:
        self.__para = miktar

    def islemSayisi(self) -> None:
        self.__para = self.__para - 10


es1 = Banka2("Sinan", 1000, "Istanbul")
es2 = Banka2("Ayse", 5000, "Erzurum")
print("1. hesaptaki para: ", es1.getPara())
es1.setPara(100)
print("set islemi sonrasi 1. hesaptaki para degisimi :", es1.getPara())


class Banka:
    def __init__(self, isim: str, para: int, adres: str) -> None:
        self.isim = isim
        self.para = para
        self.adres = adres


yedek_hesap1 = Banka("Sinan", 1000, "Istanbul")
yedek_hesap2 = Banka("Ayse", 5000, "Erzurum")
yedek_hesap2.para = yedek_hesap2.para + yedek_hesap1.para
yedek_hesap1.para = 0


class Makine:
    """Basit hesap makinesi."""

    def __init__(self, a: float, b: float) -> None:
        self.deger1 = a
        self.deger2 = b

    def topla(self) -> float:
        sonuc = self.deger1 + self.deger2
        return sonuc

    def carp(self) -> float:
        sonuc = self.deger1 * self.deger2
        return sonuc

    def cikar(self) -> float:
        return self.deger1 - self.deger2

    def bol(self) -> float:
        return self.deger1 / self.deger2


x = 5
y = 2
h: Makine = Makine(x, y)
tSonuc = h.topla()
cSonuc = h.carp()
print("toplama sonuc: {}, carpma sonucu: {}".format(tSonuc, cSonuc))


class Hayvan:
    def __init__(self, isim: str, yas: int) -> None:
        self.isim = isim
        self.yas = yas

    def getYas(self) -> int:
        return self.yas

    def getAd(self) -> str:
        return self.isim


h1 = Hayvan("dog", 2)
print("h1 in yasi :", h1.getYas())
print("h1 in isim :", h1.getAd())

h2 = Hayvan("cat", 3)
print("h2 in yasi :", h2.getYas())


class Araba:
    def __init__(self, marka: str, model: str) -> None:
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self) -> None:
        print(f"Marka: {self.marka}, Model: {self.model}")


araba1 = Araba("Toyota", "Corolla")
araba1.bilgileri_yazdir()


# 1- Asagidaki kodu yorumlayiniz (Makine sinifi yukarida tanimli)


class Dikdortgen:
    def __init__(self, genislik: float, yukseklik: float) -> None:
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self) -> float:
        return self.genislik * self.yukseklik


dikdortgen1 = Dikdortgen(5, 10)
alan = dikdortgen1.alan_hesapla()
print(f"Dikdortgenin alani: {alan}")


class Kare:
    def __init__(self, kenar: int) -> None:
        self.kenar = kenar

    def kareyi_yazdir(self) -> None:
        for _ in range(self.kenar):
            print("* " * self.kenar)


kare1 = Kare(5)
kare1.kareyi_yazdir()


class HesapMakinesi:
    def topla(self, sayi1: float, sayi2: float, sayi3: float | None = None) -> float:
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        return sayi1 + sayi2


hesap_makinesi = HesapMakinesi()
sonuc1 = hesap_makinesi.topla(10, 20)
print("Iki sayinin toplami:", sonuc1)
sonuc2 = hesap_makinesi.topla(10, 20, 30)
print("Uc sayinin toplami:", sonuc2)


class Merhaba:
    def merhaba_yazdir(self) -> None:
        print("Merhaba Dunya")


merhaba = Merhaba()
merhaba.merhaba_yazdir()


class Insan:
    def __init__(self, ad: str, yas: int) -> None:
        self.ad = ad
        self.yas = yas

    def konus(self) -> None:
        print(f"Merhaba, ben {self.ad} ve {self.yas} yasindayim.")


class Hoca(Insan):
    def __init__(self, ad: str, yas: int, sicil_no: str) -> None:
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self) -> None:
        print(f"Ben {self.ad}, dersinizi anlatacagim.")

    def ders_ver(self) -> None:
        print(f"Hoca {self.ad} ({self.sicil_no}) dersi anlatiyor.")


class Sekreter(Insan):
    def konus(self) -> None:
        print(f"Ben {self.ad}, ofis islerini yurutuyorum.")

    def randevu_al(self, kisi: str) -> None:
        print(f"{kisi} icin randevu olusturuldu.")


class Ogrenci(Insan):
    def konus(self) -> None:
        print(f"Ben {self.ad}, derse hazirlaniyorum.")

    def sinava_gir(self, ders: str) -> None:
        print(f"{self.ad}, {ders} sinavina giriyor.")


hoca = Hoca("Ahmet", 45, "H1234")
hoca.konus()
hoca.ders_ver()

sekreter = Sekreter("Ayse", 30)
sekreter.konus()
sekreter.randevu_al("Ogrenci 1")

ogrenci = Ogrenci("Mehmet", 20)
ogrenci.konus()
ogrenci.sinava_gir("Matematik")
