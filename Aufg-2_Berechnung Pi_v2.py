

#Definition Variablen
Summe = float(0)
x = int(1) #Counter
y = int(1) #Bruch
Antw = str('j')

while Antw == 'j':

    i = int(input("Hallo, bitte Grad der Iteration eingeben: "))
    dezAnzahl = int(input("Gewünschte Anzahl der anzuzeigenden Dezimalstellen eingeben: "))
    print("")
    
    #Schleife Start
    while x <= i:
        plus_minus = int(x % 2) #Entscheidung ob +/-
        #print(plus_minus)
    
        if plus_minus == 1:
            Add = float(1/y)
            #print("Addition: ",Add)
            y = y + 2
            Summe = round(float(Summe + Add),dezAnzahl)
            #print("Zwischensumme: ",Summe)
        else:
            Add = float(1/y)
            #print("Subtraktion: ",Add)
            y = y + 2
            Summe = round(float(Summe - Add),dezAnzahl)
            #print("Zwischensumme: ",Summe)
        
        Zwischensumme = round(float(Summe * 4),dezAnzahl)
        print("Ergebnis Grad",x,":",Zwischensumme)
        x = int(x + 1)
    
    #Berechnung pi (weil sonst "pi/4")
    Summe = Summe * 4

    # Zusätzliche Berechnungen
    import math
    Diff = round(math.pi - Summe,dezAnzahl)

    print("")
    print("Endergebnis",round(float(Summe),dezAnzahl))
    print("Differenz: ", abs(Diff))
    print("")
    Antw = str(input("Erneute Berechnung? Eingabe [j]: "))
    print("")
    print("==================================================")
    
    #Reset der Werte
    Summe = float(0)
    x = int(1) #Counter
    y = int(1) #Bruch

print("")
print("Und tschüss!")

print("")
print("        -/++++++++++++++++++++.   ")                                
print("      /dmmmmmmmmmmmmmmmmmmmmmm:   ")                                
print("    `smdso+ommd+++++dmmmo+++++.   ")                                
print("    od:    `mms    `dmmd`         ")                                
print("   `/`     -mm+    .mmmh          ")                                
print("           omm:    -mmms          ")                                
print("          `dmm.    +mmm+          ")                                
print("          ommm     smmm/          ")                                
print("         /mmmy     hmmm/          ")                                
print("       `ommNm/     dmmm+     o.   ")                                
print("      .hmmmmd`     dmmmd:.`-sd`   ")                                
print("      hmmmmm+      ommmmmmmmm:    ")                                
print("      +dmmdo`       /hmmmmds.     ")                                
print("        ``             ```        ")



    
    
    
