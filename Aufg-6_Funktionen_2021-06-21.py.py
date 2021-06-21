# Beispiel 6: Funktion
wb_DE = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
wb_EN = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

# Definition der einzelnen Funktionen

# Definition des Befehls "Wort hinzufügen"
def Befehl_Hinzufügen(Begriff_DE, Begriff_EN):   
    wb_DE.append(Begriff_DE)
    wb_EN.append(Begriff_EN)
    print("Der gewünschte Begriff wurde dem Wörterbuch hinzugefügt!")

# Definition des Befehls "Wort löschen"
def Befehl_Löschen():
    Wort_löschen = input ("Bitte den zu löschenden Begriff eingeben: ")
    index_löschen = 0
    while index_löschen < len(wb_DE):
        if Wort_löschen == wb_DE[index_löschen]:
            wb_EN.remove(wb_EN[index_löschen])          
            wb_DE.remove(Wort_löschen)
            print("\nDer gewünschte Begriff wurde erfolgreich gelöscht!")
            break
            
        if Wort_löschen.lower() == wb_EN[index_löschen]:
            wb_DE.remove(wb_DE[index_löschen])
            wb_EN.remove(Wort_löschen)
            print("\nDer gewünschte Begriff wurde erfolgreich gelöscht!")
            break
            
        index_löschen += 1
            
        if index_löschen == len(wb_DE):
            print("Der Suchbegriff wurde nicht gefunden, bitte erneut versuchen!")
            
# Definition des Befehls "Abfrage starten"
def Befehl_Abfrage(Suchbegriff):
    
    index_Abfrage = 0
    while index_Abfrage < len(wb_DE):
        if Suchbegriff.lower() == wb_DE[index_Abfrage].lower():
            print("\nEnglische Übersetzung: ",wb_EN[index_Abfrage])
            break
        if Suchbegriff.lower() == wb_EN[index_Abfrage].lower():
            print("\nDeutsche Übersetzung: ",wb_DE[index_Abfrage])
            break
        index_Abfrage += 1      
    if index_Abfrage == len(wb_DE):
        print("nicht gefunden")

# Definition des Befehls "Eingabe starten"
def Befehl_Eingabe():
    while True:
        Eingabe_Option = input("\nHallo! Bitte Option wählen: \nWort einfügen [e], Wort löschen [l], Abfrage starten [a], Programm beenden [b]: ")
        if Eingabe_Option.lower() == "e" or  Eingabe_Option.lower() =="l" or Eingabe_Option.lower() =="a" or Eingabe_Option.lower() =="b":
            return Eingabe_Option.lower()
        else:
            print("\nUngültige Eingabe, bitte erneut versuchen!")
    
    
while True:
    Abfrage = Befehl_Eingabe()
    if Abfrage == "e":
        Begriff_DE = input("\nBitte neuen deutschen Begriff eingeben: ")
        Begriff_EN = input("Bitte die dazu passende englische Übersetzung eingeben: ")
        Befehl_Hinzufügen(Begriff_DE, Begriff_EN)
        
    elif Abfrage == "a":
        Suchbegriff = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
        Befehl_Abfrage(Suchbegriff)
    elif Abfrage == "l":
        Befehl_Löschen()
    elif Abfrage == "b":
        print("\nVorgang auf Wunsch des Benutzers abgebrochen!\nAuf Wiedersehen!")
        break 