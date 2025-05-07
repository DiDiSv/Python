def calculeaza_greutatea_ideala(sex, inaltime, varsta):
    if sex == "M":
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
    elif sex == "F":
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)
    return round(greutate_ideala, 2)

while True:
    try:
        varsta = int(input("Introduceți vârsta (20-120): "))
        if not (20 < varsta < 120):
            print("Vârsta trebuie să fie între 21 și 119 ani.")
            continue

        inaltime = int(input("Introduceți înălțimea (150-220 cm): "))
        if not (150 <= inaltime <= 220):
            print("Înălțimea trebuie să fie între 150 și 220 cm.")
            continue

        greutate = float(input("Introduceți greutatea actuală (45-300 kg): "))
        if not (45 <= greutate <= 300):
            print("Greutatea trebuie să fie între 45 și 300 kg.")
            continue

        sex = input("Introduceți sexul (M/F): ").strip().upper()
        if sex not in ["M", "F"]:
            print("Sexul trebuie să fie 'M' sau 'F'.")
            continue

        greutate_ideala = calculeaza_greutatea_ideala(sex, inaltime, varsta)
        print(f"Greutatea ideală este: {greutate_ideala} kg")

        diferenta = greutate - greutate_ideala
        if diferenta > 0:
            print("Trebuie să slăbești.")
        elif diferenta < 0:
            print("Trebuie să adaugi în greutate.")
        else:
            print("Felicitări! Ai greutatea ideală.")
        break
    except ValueError:
        print("Introduceți valori numerice valide.")
