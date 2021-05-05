# Standard Wörterbücher
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

# Start: Abfrage
auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()

# Hauptschleife
while True:
    if auswahl == 'e': # Option: Neuer Eintrag
        
        # Ausgabe Inhalt der aktuellen Wörterbücher
        print("\nÜbersicht - aktuelle Einträge:")
        print("Wörterbuch Deutsch: ", woerterbuch_deutsch)
        print("Wörterbuch English: ", woerterbuch_english)
    
        # Eingabe neues Wort
        wort_neu = input("\nEingabe des neuen Wortes: ")
    
        # Abfrage, ob Eingabe englisch oder Deutsch
        while True:
                DE_EN = input("Eingabe, ob Deutsch [D] oder Englisch [E]? ").lower()
                if DE_EN == "d" or DE_EN == "e":
                    break
                else:
                    print("\nFehler, unerlaubter Eingabebefehl!")
        
        # Abfrage der Übersetzung gemäß ausgewählter Sprache
        if DE_EN == "d":
            wort_neu_DE = wort_neu
            wort_neu_EN = input("Bitte englisches Äquivalent eingeben: ")
            print("\nEingegebens Wort: ", wort_neu_DE,"(DE)")
            print("Übersetzung: ", wort_neu_EN, "(EN)\n")
        else:
            wort_neu_EN = wort_neu
            wort_neu_DE = input("Bitte deutsches Äquivalent eingeben: ")
            print("\nEingegebens Wort: ", wort_neu_EN, "(EN)")
            print("Übersetzung: ", wort_neu_DE, "(DE)\n")
            
        # Eintrag der neuen Wörter in Wörterbücher
        woerterbuch_deutsch.append(wort_neu_DE)
        woerterbuch_english.append(wort_neu_EN)
    
        # Ausgabe der aktualisierten Wörterbücher
        print("Aktualisiertes Wörterbuch:")
        print("Wörterbuch Deutsch: ", woerterbuch_deutsch)
        print("Wörterbuch English: ", woerterbuch_english)

        # Erneute Start-Abfrage
        auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()

    elif auswahl == 'l': # Option: Wort löschen
    
        # Ausgabe der aktuellen Wörterbücher
        print("\nÜbersicht - aktuelle Einträge:")
        print("Wörterbuch Deutsch: ", woerterbuch_deutsch)
        print("Wörterbuch English: ", woerterbuch_english)
        
        # Eingabe zu löschendes Wort (unabhängig Groß-/Kleinschreibung)
        wort_löschen = input("\nZu löschendes Wort eingeben: ").lower()
        
        # Bestimmung des max. Index
        index_DE = len(woerterbuch_deutsch)-1
        index_EN = len(woerterbuch_english)-1
        
        if index_DE <= index_EN:
            index_max = index_DE
        else:
            index_max = index_EN
        
        # Start-Index
        index_löschen = 0
        
        # Ermittlung gesuchter Index
        while index_löschen <= index_max:
            wort_del_suche_DE = woerterbuch_deutsch[index_löschen].lower()
            wort_del_suche_EN = woerterbuch_english[index_löschen].lower()
            
            if wort_löschen == wort_del_suche_DE or wort_löschen == wort_del_suche_EN:
                print("Gefunden, Eintrag wurde gelöscht!")
                break
            else:
                index_löschen += 1
        
        # Löschvorgang bzw. Ausgabe "nicht gefunden"
        if index_löschen <= index_max:
            wort_löschen_DE = woerterbuch_deutsch[index_löschen]
            wort_löschen_EN = woerterbuch_english[index_löschen]
            woerterbuch_deutsch.remove(wort_löschen_DE)
            woerterbuch_english.remove(wort_del_suche_EN)
            auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()
        else:
            print("Der gewünschte Suchbegriff wurde nicht gefunden!")
            auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()
        
    elif auswahl == "a": # Option: Wort abfragen
        
        # Bestimmung des max. Index
        index_DE = len(woerterbuch_deutsch)-1
        index_EN = len(woerterbuch_english)-1
        
        if index_DE <= index_EN:
            index_max = index_DE
        else:
            index_max = index_EN  
        
        # Eingabe Suchbegriff, Definition der Listen
        suchbegriff = input("\nHallo, bitte Suchbegriff eingeben : ")
        
        # Start-Index
        index = 0
        wort = suchbegriff.lower()
        
        # Ermittlung gesuchter Index
        while index <= index_max:
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
                
        # Ausgabe, sofern kein Suchergebnis
        if index > index_max:
            print("Keine Übersetzung gefunden!")
            auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()
        else:
            auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? Eingabe: ").lower()
        
    elif auswahl == "b": # Option: Programm beenden
        break
    
    elif auswahl == "z": # Option: Wörterbücher zurücksetzen
        
        print("\nWörterbücher auf Standard zurückgesetzt!")
        woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
        woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
        print(woerterbuch_deutsch)
        print(woerterbuch_english)
        
        auswahl = input("\nWas möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? ").lower()
        
    else: # Sofern Start-Eingabe ungültig
        print("\nUngültige Eingabe!\n")
        auswahl = input("Was möchten Sie tun?\nWort einfügen [E], Wort löschen [L], Abfrage [A], Wörterbuch zurücksetzen [Z] oder Beenden [B]? ").lower()

# Ende Programmcode
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Programm auf Wunsch abgebrochen, tschüss!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 


        




