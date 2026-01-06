### Ursprüngliche Idee war eine Zuganzeige, da mir im Zug langweilig war.
### Hier gibt es nun mehrere interaktive Möglichkeiten rund um die
### Verspätung im ÖPNV

import random
import datetime
from datetime import timedelta

### Variablen für die Uhrzeit

jetzt = datetime.datetime.now()
uhrzeit_text = jetzt.strftime("%H:%M") 
print("Aktuelle Zeit:", uhrzeit_text)

### Ticketpreis des Fahrgastes

ticketpreis = input("Wieviel hast du für das Ticket bezahlt?")
ticketpreis = int(ticketpreis)

### Verspaetungswürfel

verspaetung = random.randint(0, 60)

ankunft_neu = jetzt + datetime.timedelta(minutes=verspaetung)
print(f"Ihr Zug hat {verspaetung} Minuten Verspätung und kommt an um {ankunft_neu}")

### Gutschrift, falls eine Verspätung auftritt
 
if ticketpreis > 25 and verspaetung > 30:
    gutschrift = ticketpreis / 15
    print(f"Sie haben eine Gutschrift in Höhe von {gutschrift} erhalten.")
else:
    print(f"Sie haben keine Gutschrift erhalten, da sie die Bedingungen nicht erfüllen.")

### Gruende für die Verspaetung

gruende = {"Wetter": "Die Witterungsbedingungen sind schlecht.",
           "Fahrgäste": "Die Fahrgäste haben Mist gebaut."}

### Komplette Anzeige von allem

