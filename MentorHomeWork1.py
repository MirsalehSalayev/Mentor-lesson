#task1SESVERME
yas = int(input("Yaş "))

if yas >= 18:
    print("Səs ver")
else:
    print("Səs vermənmersen")

#task2DUZBUCAQ
en = float(input("Eni "))
uzunluq = float(input("Uzunluğ "))

sahe = en * uzunluq

print(f"Düzbucaqlının sahəsi: {sahe}")

#task3HAVATEMP
temp = float(input("Hazırkı temperatur"))

if temp > 30:
    print("Hava çox istidir")
elif 15 <= temp <= 30:
    print("Hava idealdır")
else:
    print("Hava soyuqdur")

#TASK4BOYUK EDED
eded1 = int(input("Birinci ədəd "))
eded2 = int(input("İkinci ədəd "))

if eded1 > eded2:
    print(f"{eded1} daha böyükdür")
elif eded2 > eded1:
    print(f"{eded2} daha böyükdür")
else:
    print("Ədədlər bərabərdir")

#TASK5KALK
a = float(input("Birinci rəqəm "))
b = float(input("İkinci rəqəm: "))
operator = input("Operator + və ya ")

if operator == "+":
    netice = a + b
    print(f"{a} + {b} = {netice}")
elif operator == "-":
    netice = a - b
    print(f"{a} - {b} = {netice}")
else:
    print("Yalnız '+' və ya '-' operatoru daxil edin!")
#TASK6TAMEDED
eded = int(input("tam eded "))

qalig = eded % 2

if qalig == 0:
    print("Bu ədəd cütdür")
else:
    print("Bu ədəd təkdir")