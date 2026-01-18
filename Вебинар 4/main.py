msc_price = 13_000
spb_price = 10_000
ekb_price = 8_000  # Можно добавить _ в числе и python будет это игнорировать

dist = input("Введите пункт назначения (msc, spb, ekb): ")
adults = int(input("Введите количество взрослых: "))
kids = int(input("Введите количество детей: "))

if dist == "msc":
    price = msc_price * (2 * adults + kids) // 2
elif dist == "spb":
    price = spb_price * (2 * adults + kids) // 2
elif dist == "ekb":
    price = ekb_price * (2 * adults + kids) // 2

print("Цена поездки: ", price)

