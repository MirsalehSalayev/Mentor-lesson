# ── Task 1 ──────────────────────────────────────────────────────
rengler = ["Qırmızı", "Yaşıl", "Mavi"]
for reng in rengler:
    print(reng)

# ── Task 2 ──────────────────────────────────────────────────────
reqemler = [12, 45, 7, 23, 9, 88, 31]
for reqem in reqemler:
    if reqem % 2 != 0 and reqem > 20:
        print(f"Şanslı rəqəm tapıldı: {reqem}")
        break

# ── Task 3 ──────────────────────────────────────────────────────
balanslar = [100, -20, 50, -5, 200, 0]
for balans in balanslar:
    if balans < 0:
        continue
    print(balans)

# ── Task 4 ──────────────────────────────────────────────────────
n = int(input("Rəqəm daxil et: "))
for i in range(1, n + 1):
    print(f"{i}-in kubu: {i ** 3}")

# ── Task 5 ──────────────────────────────────────────────────────
qiymetler = [10, 20, 30, 40, 50]
for index, qiymet in enumerate(qiymetler):
    if index % 2 == 0:
        print(f"Məhsul {index}: Yeni qiymət {qiymet - 2} manat")

# ── Task 6 ──────────────────────────────────────────────────────
eded, cem = 1, 0
while eded <= 10:
    cem += eded
    eded += 1
print(f"1-dən 10-a qədər ədədlərin cəmi: {cem}")

# ── Task 7 ──────────────────────────────────────────────────────
meyveler = ["Alma", "Banan", "Alça", "Portağal"]
for meyve in meyveler:
    print(meyve)
    if meyve == "Alça":
        print("Alça tapıldı!")

# ── Task 8 ──────────────────────────────────────────────────────
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ── Task 9 ──────────────────────────────────────────────────────
balans, ay = 100, 0
while balans <= 500:
    ay += 1
    balans *= 1.1
    print(f"Ay {ay}: {balans:.2f} AZN")

# ── Task 10 ─────────────────────────────────────────────────────
while True:
    sifre = input("Şifrə daxil et: ")
    if len(sifre) < 8:
        print("Şifrə çox qısadır!")
    elif "123" in sifre:
        print("Şifrə çox sadədir!")
    else:
        print("Şifrə uğurla qeydə alındı")
        break

# ── Task 11 ─────────────────────────────────────────────────────
dogru_sifre = "secret123"
while input("Şifrəni daxil et: ") != dogru_sifre:
    print("Yenidən cəhd edin")
print("Giriş uğurludur")

# ── Task 12 ─────────────────────────────────────────────────────
import random

gizli = random.randint(1, 100)
cehd_sayi = 3

while cehd_sayi > 0:
    texmin = int(input(f"Təxmininizi daxil edin ({cehd_sayi} cəhd qalıb): "))
    if texmin == gizli:
        print("Təbriklər! Rəqəmi tapdınız!")
        break
    elif texmin < gizli:
        print("Daha böyük!")
    else:
        print("Daha kiçik!")
    cehd_sayi -= 1
else:
    print(f"Cəhdlər bitdi! Gizli rəqəm {gizli} idi.")