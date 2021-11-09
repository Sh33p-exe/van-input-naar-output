personen = int(input("Hoeveel personen: "))

ticketPrijs = int(input("Ticket prijs in centen: "))/100
ticketTotaal = (ticketPrijs*personen)

VRSeatPrijs = int(input("VRSeat prijs: "))/100
VRSeatTotaal = (VRSeatPrijs*personen)

volledigePrijs = (ticketTotaal+VRSeatTotaal)

print(" ----------------------------------------------------")
print("|   Welkom in de speelhal!")
print("|   Jullie zijn met " + str(personen) + " mensen")
print("|   Met de Ticket prijs van €" + str(ticketPrijs) + " wordt het totaal €" + str(ticketTotaal))
print("|   En met de VRSeat prijs van €" + str(VRSeatPrijs) + " wordt het totaal voor de VRSeat €" + str(VRSeatTotaal))
print("|   De totale prijs van vandaag is €" + str(volledigePrijs) + " (" + str(ticketTotaal) + " + " + str(VRSeatTotaal) + " = " + str(volledigePrijs) + ")")
print(" ----------------------------------------------------")