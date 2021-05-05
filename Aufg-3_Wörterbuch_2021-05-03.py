# 1) Eingabe Suchbegriff
# 2) Bestimmung der Gesamtanzahl der Elemente der Liste (= max. Index)
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden, --> Index speichern
# 5) Zugriff auf Listenelement[Index] in Liste (englisches Wörterbuch)

# Zusatz: Eingabe, wahlweise deutscher/englischer Begriff mit entsprechender Ausgabe!

# Eingabe Suchbegriff, Definition der Listen
suchbegriff = input("Hallo, bitte Suchbegriff eingeben :")
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

# Ermittlung der Längen der Listen + Umwandlung als Index
Länge_DE = len(woerterbuch_deutsch)-1
Länge_EN = len(woerterbuch_english)-1

if Länge_DE <= Länge_EN:
    Länge_max = Länge_DE
else:
    Länge_max = Länge_EN   

index = 0
wort = suchbegriff.lower()

while index <= Länge_max:    
    wort_vergleich_DE = woerterbuch_deutsch[index].lower()
    wort_vergleich_EN = woerterbuch_english[index].lower()
    if wort == wort_vergleich_DE:
        print("Übersetzung: ", woerterbuch_english[index], "(EN)")
        break
    elif wort == wort_vergleich_EN:
        print("Übersetzung: ", woerterbuch_deutsch[index], "(DE)")
        break
    else:
        index += 1
        
if index > Länge_max:
    print("Keine Übersetzung gefunden!")
else:
    print("Tschüss!")
        




