# Exercise 1 - Alış-veriş Siyahısı
market_list = ["çörək", "süd", "yumurta"]
market_list.append("yağ")
market_list.insert(0, "meyvə")
market_list.remove("süd")
print("Son vəziyyət:", market_list)


# Exercise 2 - Tuple
haqqimda = ("Əli", 2003, "Bakı")
print("2-ci element (indeks 1):", haqqimda[1])

try:
    haqqimda[0] = "Vəli"
except TypeError as e:
    print("Xəta:", e)


# Exercise 3 - Tuple Birləşdirmə
isti_rengler  = ("qırmızı", "narıncı")
soyuq_rengler = ("mavi", "yaşıl")
butun_rengler = isti_rengler + soyuq_rengler
print("Bütün rənglər:", butun_rengler)


# Exercise 4 - Siyahıda Axtarış
diller = ["Python", "Java", "C++", "JavaScript"]
dil = input("Bir proqramlaşdırma dili daxil edin: ")
if dil in diller:
    print("Bu dil siyahıda var")
else:
    print("Siyahıda tapılmadı")


# Exercise 5 - Slicing
reqemler = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("İlk 3 element:", reqemler[:3])
print("Son 3 element:", reqemler[-3:])
print("Orta [4,5,6]:", reqemler[4:7])


# Exercise 6 - Tərsinə Çevirmə
herfler = ["P", "y", "t", "h", "o", "n"]
print("Tərsinə:", herfler[::-1])


# Exercise 7 - Cüt Ədədlər
cut_ededler = [x for x in range(1, 21) if x % 2 == 0]
print("Cüt ədədlər:", cut_ededler)


# Exercise 8 - Böyük Hərf
adlar = ["eli", "vəli", "ayşə"]
print("Böyük hərf:", [ad.upper() for ad in adlar])


# Exercise 9 - Qiymətlər
qiymetler = [12, 45, 67, 23, 90, 11]
qiymetler.sort()
qiymetler.remove(min(qiymetler))
qiymetler.remove(max(qiymetler))
print("Qalan elementlər:", qiymetler)
print("Elementlərin sayı:", len(qiymetler))


# Exercise 10 - Şəhərlər
seherler = ["Bakı", "Gəncə", "Sumqayıt"]
seherler.append("Şəki")
seherler.remove("Gəncə")
seherler.sort()
print("Siyahı:", seherler)
print("Element sayı:", len(seherler))


# Exercise 11 - Tuple Dəyişdirmə Hiləsi
aylar = ("Yanvar", "Fevral", "Mart")
aylar_list = list(aylar)
aylar_list.append("Aprel")
aylar = tuple(aylar_list)
print("Yeni tuple:", aylar)


# Exercise 12 - Tələbə Qiymətləri
qiymetler = [85, 42, 90, 75, 30, 95, 60, 40]
qiymetler.sort(reverse=True)

kesilen = [q for q in qiymetler if q < 51]
print(f"Kəsilmiş tələbələrin sayı: {len(kesilen)} nəfər → {kesilen}")

qiymetler.remove(max(qiymetler))
qiymetler.remove(min(qiymetler))
orta = sum(qiymetler) / len(qiymetler)
print(f"Qalan qiymətlər: {qiymetler}")
print(f"Orta göstərici: {orta:.2f}")


# Exercise 13 - Unikal Ədədlər
ededler = [1, 2, 2, 3, 4, 4, 4, 5, 6, 1]
unikal_ededler = []

for edet in ededler:
    if edet not in unikal_ededler:
        unikal_ededler.append(edet)

print("Orijinal:", ededler)
print("Unikal:", unikal_ededler)