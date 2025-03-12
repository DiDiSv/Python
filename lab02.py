# Sarcina 1
# Lista
lista = [10, 20, 30, 40, 50]
print("Prima valoare:", lista[0])
print("A treia valoare:", lista[2])
lista[1] = 25  
print("Lista modificată:", lista)

sublista = lista[1:4] 
print("Sublista extrasă:", sublista)

# Aplicare metodă, funcții și operatori
lista.append(60) 
print("Lista după append:", lista)

lungime = len(lista) 
print("Lungimea listei:", lungime)

suma_elemente = sum(lista) 
print("Suma elementelor:", suma_elemente)

print("30 este în listă?", 30 in lista) 
print("100 nu este în listă?", 100 not in lista) 
print("Lista dublată:", lista * 2)  

# Tuplu
tuplu = (5, 15, 25, 35, 45)
print("Tipul de date:", type(tuplu))
print("Prima valoare:", tuplu[0])
print("Ultima valoare:", tuplu[-1])

subtuplu = tuplu[1:4]  
print("Subtuplu extras:", subtuplu)

print("Lungimea tuplului:", len(tuplu))  
print("Valoarea maximă:", max(tuplu))  
print("Valoarea minimă:", min(tuplu)) 

# Set
multime = {1, 2, 2, 3, 4, 4, 5}  
print("Mulțimea:", multime)
multime.add(6)  
print("Mulțimea după adăugare:", multime)
print("Lungimea mulțimii:", len(multime))  

# Dicționar
dict_text = {"nume": "Ana", "oraș": "București"}
dict_num = {1: "Luni", 2: "Marți", 3: "Miercuri"}
print("Element din dict_text:", dict_text["nume"])
print("Element din dict_num:", dict_num[2])

dict_text.update({"vârstă": 25}) 
print("Dicționar actualizat:", dict_text)

dict_num.pop(3)  
print("Dicționar numeric după eliminare:", dict_num)

print("Cheile dicționarului text:", dict_text.keys())  
print("Valorile dicționarului numeric:", dict_num.values())  

# Conversie între tipuri de date
lista_to_tuplu = tuple(lista)
print("Lista convertită în tuplu:", lista_to_tuplu)
tuplu_to_lista = list(tuplu)
print("Tuplul convertit în listă:", tuplu_to_lista)

# Sarcina 2
produse = ["Mere", "Pere", "Banane"]
preturi = [5, 8, 6]

for produs, pret in zip(produse, preturi):
    print("Produsul {} costă {} lei".format(produs, pret))

varsta = int(input("Introduceți vârsta: "))
varsta_viitoare = varsta + 5
print("În 5 ani veți avea " + str(varsta_viitoare) + " ani.")

cuvinte = ["python", "jocuri", "programare"]
print("'python' este în listă?", "python" in cuvinte)
print("'java' nu este în listă?", "java" not in cuvinte)
