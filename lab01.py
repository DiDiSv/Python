#sub 1
#ex1

name = input("Bună! Te rog să introduci numele tău: ")
print(f"Salut, {name}!")

#ex2

numar_intreg = 19
numar_real = 16.21
text_scurt = "Izvorul nopţii"
text_lung = """Frumoaso, ţi-s ochii-aşa de negri încât seara
când stau culcat cu capu-n poala ta îmi pare că ochii tăi, adânci, sunt izvorul
din care tainic curge noaptea peste văi şi peste munţi şi peste seşuri
acoperind pământul c-o mare de-ntuneric. Aşa-s de negri ochii tăi, lumina mea."""

#ex3

print(f"Tipul de date a variabilei 'numar_intreg' este: {type(numar_intreg)}")
print(f"Tipul de date a variabilei 'text_scurt' este: {type(text_scurt)}")

#ex4

print(f"Lungimea textului scurt este: {len(text_scurt)}")

#ex5

text_mare = text_scurt.upper()
print(f"Text cu litere majuscule: {text_mare}")

# ex6. 

subtext = text_lung[14:20]
print(f"Subsirul taiat din textul lung este:{subtext}")

#ex7. 

# string.format()

print("Mesaj folosind format: {0} are varsta de {1} ani.".format(name, numar_intreg))

# f-string

varsta = 20
print(f"Mesaj folosind f-string: Pe 1 Martie {name} implineste {varsta} ani.")

#sub 2

#a

#txt = "More results from text..."
#substr = txt[4:12]
#print(substr)
#print(substr.strip())

# rezultatul va fi: results, deoarece substr = results, substr.strip scoate spatiile, deci se afiseaza doar "results"

#b

#txt = "More results from text..."
#print(txt.split())

#se impart cuvintele aparte, deci va fi o lista de cuvinte: ['More', 'results', 'from', 'text']

#c

#age = 36
#txt = "My name is Mary, and I am {}"
#print(txt.format(age))

# va afisa urmatoarele: My name is Mary, and  I am 36, fiindca in loc de {} se include variabila age, datorita txt.format
