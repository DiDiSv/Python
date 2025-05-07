cat_age_dict = {
    1: "6 luni", 2: "10 luni", 3: "2 ani", 4: "5 ani", 5: "8 ani",
    6: "14 ani", 7: "15 ani", 8: "16 ani", 9: "16 ani", 10: "17 ani", 11: "17 ani"
}

while True:
    raspuns = input("Pisica are mai puțin de un an? (Da/Nu): ").strip().lower()
    if raspuns in ["da", "yes"]:
        while True:
            try:
                luni = int(input("Introduceți vârsta pisicii în luni (1-11): "))
                if luni in cat_age_dict:
                    print(f"Vârsta în ani umani: {cat_age_dict[luni]}")
                    break
                else:
                    print("Introduceți o valoare între 1 și 11.")
            except ValueError:
                print("Introduceți un număr întreg.")
        break

    elif raspuns in ["nu", "no"]:
        while True:
            try:
                ani = int(input("Introduceți vârsta pisicii (1-35): "))
                if not (1 <= ani < 35):
                    print("Vârsta trebuie să fie între 1 și 34.")
                    continue

                if ani == 1:
                    uman = 18
                elif ani == 2:
                    uman = 25
                elif 3 <= ani <= 15:
                    uman = 25 + (ani - 2) * 4
                else:
                    uman = 25 + 13 * 4 + (ani - 15) * 3  

                print(f"În ani omenești, pisica are {uman} ani.")
                break
            except ValueError:
                print("Introduceți un număr întreg.")
        break
    else:
        print("Răspundeți cu 'Da' sau 'Nu'.")
