def endirim_hesabla(qiymət, endirim_faizi):
    return qiymət * (1 - endirim_faizi / 100)


def kub_hecm(tərəf):
    return f"{tərəf} ölçülü kubun həcmi: {tərəf ** 3}"


def soz_say(cümlə):
    return len(cümlə.split())


def bas_herfle_yaz(siyahı):
    return [söz.capitalize() for söz in siyahı]


def yasa_gore_salam(ad, soyad, yaş):
    if yaş < 18:
        return f"Salam {ad} {soyad}, hələ yetkinlik yaşına çatmamısan!"
    elif yaş <= 65:
        return f"Salam {ad} {soyad}, xoş gəldin!"
    else:
        return f"Hörmətli {ad} {soyad}, xoş gəldiniz!"


def kalkulyator(a, b, əməliyyat):
    if əməliyyat == "+":
        return a + b
    elif əməliyyat == "-":
        return a - b
    elif əməliyyat == "*":
        return a * b
    elif əməliyyat == "/":
        if b == 0:
            return "Xəta: Sıfıra bölmək olmaz"
        return a / b
    else:
        return "Xəta: Bilinməyən əməliyyat"


def en_boyuk_element(siyahı):
    return f"Siyahıdakı ən böyük ədəd: {max(siyahı)}"


def menfileri_tap(siyahı):
    return [x for x in siyahı if x < 0]


if __name__ == "__main__":
    print(endirim_hesabla(200, 25))
    print(kub_hecm(3))
    print(soz_say("Salam necəsən yaxşıyam"))
    print(bas_herfle_yaz(["python", "süni", "intellekt"]))
    print(yasa_gore_salam("Murad", "Əliyev", 17))
    print(yasa_gore_salam("Murad", "Əliyev", 30))
    print(yasa_gore_salam("Murad", "Əliyev", 70))
    print(kalkulyator(10, 2, "/"))
    print(kalkulyator(10, 0, "/"))
    print(en_boyuk_element([4, 17, 9, 3]))
    print(menfileri_tap([3, -1, -7, 5, -2]))