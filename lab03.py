# 1. Funcție lambda pentru salut utilizator

greet_user = lambda name: print('Hello My Dear,', name)
user_name = input("What is your name? ")
greet_user(user_name)

# 2. Sortarea unei liste de tupluri

lista = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (9, 3), (12, 44)]
lista_sortata = sorted(lista, key=lambda x: x[1])
print("Lista sortată după al doilea element:", lista_sortata)

# 3. Propria funcție lambda – verificare paritate

este_par = lambda x: x % 2 == 0
print("Este 4 par?", este_par(4))
print("Este 5 par?", este_par(5))
print("Este 10 par?", este_par(10))
print("Este 17 par?", este_par(17))

# 4. Definirea și apelarea funcțiilor clasice

# a) Funcție fără parametri
def salut():
    print("Salut, bine ai venit la laborator!")
salut()

# b) Funcție cu parametri
def aduna(a, b):
    return a + b
rez_adunare = aduna(10, 5)
print("Rezultatul adunării 10 + 5 este:", rez_adunare)

# c) Funcție cu parametri și valoare implicită
def salutare(nume="Student"):
    print("Bine ai venit,", nume)
salutare()
salutare("Maria")

# 5. Funcții cu și fără return

print("Funcții care returnează sau nu o valoare")
def inmulteste(a, b):
    return a * b
rez_inmultire = inmulteste(6, 7)
print("Rezultatul înmulțirii 6 * 7 este:", rez_inmultire)
def afisare_mesaj():
    print("Aceasta este o funcție care doar afișează un mesaj.")
afisare_mesaj()

