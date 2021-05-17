# Ändern Sie das Wörterbuch-Beispiel so,
# dass Sie anstelle der Listen Dictionaries verwenden.
# Mittels try/except soll die Abfrage nach nicht-existenten
# Begriffen fehlerfrei gestaltet werden, bzw. die wahlweise
# Eingabe von deutschen od. englischen Begriffen möglich sein.
# Ein Ergänzung bzw. das Löschen von Begriffen ist nicht gefordert.

# Definition Wörterbücher DE/EN
wb_DE = {"Apfel": "apple",
        "Birne": "pear",
        "Kirsche": "cherry",
        "Melone": "melon",
        "Marille": "apricot",
        "Pfirsich": "peach"}

wb_EN = {"apple": "Apfel",
        "pear": "Birne",
        "cherry": "Kirsche",
        "melon": "Melone",
        "apricot": "Marille",
        "peach": "Pfirsich"}

print("Übersicht bestehendes Wörterbuch:\n",wb_DE, "\n")

wb_länge = len(wb_DE)
# print(wb_länge)

index = 0
suchbegriff = input("Hallo, bitte Suchbegriff eingeben: ")

while index <= 1:
    try:
        if index == 0: 
            print("Übersetzung: ", wb_DE[suchbegriff], "(EN)")
            break
        else:
            print("Übersetzung: ", wb_EN[suchbegriff], "(DE)")
            break
    except KeyError:
        if index == 0:    
            index = 1
        else:
            print("Kein Suchergebnis!")
            index = 2
    
print("\nProgrammende, tschüss!")     
