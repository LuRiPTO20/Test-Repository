# Schleifen-/Zählvariable: i, j, k ...

"""Addieren Sie in einer Schleife(!) die Zahlen von 1 bis 100 und geben Sie das Ergebnis aus"""

Antw = str('j')

while Antw == 'j':
    
    Summe = 0
    x = 1
    while x <= 100:
        Summe += x
        x += 1
        print(Summe)
    print("")
    Antw = input(str("Erneute Ausführung der Schleife? [j] >>> "))
    
