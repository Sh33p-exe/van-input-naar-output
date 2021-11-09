croissantHoeveelheid = int(input("Hoeveel croissants: "))
croissantPrijs = int(input("Croissant prijs in centen: "))/100
croissantTotaal = (croissantHoeveelheid*croissantPrijs)

stokbroodHoeveelheid = int(input("Hoeveel stokbroden: "))
stokbroodPrijs = int(input("Stockbrood prijs in centen: "))/100
stokbroodTotaal = (stokbroodHoeveelheid*stokbroodPrijs)

bonnenHoeveelheid = int(input("Hoeveel kortings bonnen: "))
bonnenKorting = int(input("Korting in centen: "))/100
bonnenTotaal = (bonnenHoeveelheid*bonnenKorting)

volledigePrijs = (croissantHoeveelheid*croissantPrijs+stokbroodHoeveelheid*stokbroodPrijs-bonnenHoeveelheid*bonnenKorting)

print(" ----------------------------------------------------")
print("|   Met de " + str(croissantHoeveelheid) + " croissantjes kosten intotaal: €" + str(croissantTotaal) + ",")
print("|   de " + str(stokbroodHoeveelheid) + " stokbroodjes kosten intotaal: €" + str(stokbroodTotaal))
print("|   en de " + str(bonnenHoeveelheid) + " kortingsbonnen met de waarde van: €" + str(bonnenKorting) + " Hebben intotaal een korting van: €" + str(bonnenTotaal))
print("|   Kom je intotaal uit op een bedrag van €" + str(volledigePrijs) + " (" + str(croissantTotaal)  + " + " + str(stokbroodTotaal) + " - " + str(bonnenTotaal) + " = " + str(volledigePrijs) + ")")
print(" ----------------------------------------------------")