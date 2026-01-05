import random
import datetime
from datetime import timedelta

### Variablen für die Uhrzeit

jetzt = datetime.datetime.now()
uhrzeit_text = jetzt.strftime("%H:%M") 
print("Aktuelle Zeit:", uhrzeit_text)

### Verspaetungswürfel

verspaetung = random.randint(0, 60)

ankunft_neu = jetzt + datetime.timedelta(minutes=verspaetung)
print(f"Ihr Zug hat {verspaetung} Minuten Verspätung und kommt an um {ankunft_neu}")

### Gruende für die Verspaetung

### Komplette Anzeige von allem
