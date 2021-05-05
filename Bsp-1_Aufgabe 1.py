"""
Aufgabe 1:
Schreiben Sie ein Python-Programm, das
1) Den Benutzer grüßt
2) Eine erste Zahl entgegennimmt
3) Eine zweite Zahl entgegennimmt
4) die Summe der beiden Zahlen berechnet und ausgibt
5) die Differenz der kleineren von der größeren Zahl berechnet und ausgibt
6) die Produkt der beiden Zahlen berechnet und ausgibt
7) den Quotient kleinere Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)
"""

Name = str(input("Servus! Bitte Namen eingeben: "))
print("Hallo",Name,"!")
print("")

# Eingabe der Variablen
zahl1 = int(input("Eingabe der ersten Zahl: "))
print("Eingabe:", zahl1)

zahl2 = int(input("Eingabe der zweiten Zahl: "))
print("Eingabe:", zahl2)
print("")

if zahl1 == zahl2:
    print("Zahl 1 und Zahl 2 sind gleich!")
    print("")
    a = int(zahl1)
    b = int(zahl2)
elif zahl1 > zahl2:
    print("Zahl 1 ist größer!")
    print("")
    b = int(zahl1)
    a = int(zahl2)
elif zahl2 > zahl1:
    print("Zahl 2 ist größer!")
    print("")
    a = int(zahl1)
    b = int(zahl2)

# Berechnung Summe
Ergebnis_Summe = a + b
print("Ergebnis Summe:", Ergebnis_Summe)

# Berechnung Differenz
Ergebnis_Diff = b - a
print("Ergebnis Differenz größere minus kleinere Zahl:", Ergebnis_Diff)

# Berechnung Produkt
Ergebnis_Produkt = a * b
print("Ergebnis Produkt", Ergebnis_Produkt)

# Berechnung Quotient
Ergebnis_Quotient = b / a
print("Ergebnis Quotient größere durch kleinere Zahl:", Ergebnis_Quotient)
#print("")

print("")
print("Have a nice day! :)")
