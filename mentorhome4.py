# ── Exercise 1 ───────────────────────────────────────────────────
filmler = ["Inception", "Interstellar", "The Matrix"]
filmler.append("Oppenheimer")
filmler[0] = "The Dark Knight"
print(len(filmler))

# ── Exercise 2 ───────────────────────────────────────────────────
melumat = ("Anar", 25, "Bakı")
for element in melumat:
    print(element)
print(len(melumat))

# ── Exercise 3 ───────────────────────────────────────────────────
elifba = ["a","b","c","d","e","f","g","h"]
print(elifba[:4])        # → ['a', 'b', 'c', 'd']
print(elifba[-3:])       # → ['f', 'g', 'h']
print(elifba[2:5])       # → ['c', 'd', 'e']

# ── Exercise 4 ───────────────────────────────────────────────────
temperaturlar = [0, 20, 37, 100]
fahrenheit = [c * 9/5 + 32 for c in temperaturlar]
print(fahrenheit)        # → [32.0, 68.0, 98.6, 212.0]

# ── Exercise 5 ───────────────────────────────────────────────────
sehерler = ("Bakı", "Gəncə", "Sumqayıt")
sehерler = list(sehерler)
sehерler += ["Lənkəran", "Şəki"]
sehерler.sort()
print(tuple(sehерler))

# ── Exercise 6 ───────────────────────────────────────────────────
sinif_a = [75, 90, 55]
sinif_b = [80, 45, 95, 60]
butun_qiymetler = sorted(sinif_a + sinif_b, reverse=True)
kecenler = [q for q in butun_qiymetler if q >= 60]
print(len(kecenler))

# ── Exercise 7 ───────────────────────────────────────────────────
cumle = "python proqramlaşdırma dillərin ən populyarı hesab olunur"
sozler = cumle.split()
qisa_sozler = []
for soz in sozler:
    print(f"{soz} — {len(soz)} hərf")
    if len(soz) < 3:
        qisa_sozler.append(soz)
print(qisa_sozler)

# ── Exercise 8 ───────────────────────────────────────────────────
qiymetler = sorted([85, 42, 90, 75, 30, 95, 60, 40], reverse=True)
kesilen = sum(1 for q in qiymetler if q < 51)
print(f"Kəsildi: {kesilen} nəfər")
qiymetler.pop(0)
qiymetler.pop(-1)
print(sum(qiymetler) / len(qiymetler))