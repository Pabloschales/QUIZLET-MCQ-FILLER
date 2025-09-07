# Schritt 3: Test-Code für Einlesen und Zählen der Karten

dateipfad = "antworten.txt"  # Oder passe den Pfad an, falls die Datei woanders liegt

with open(dateipfad, encoding="utf-8") as f:
    zeilen = [line.strip() for line in f if line.strip() and line.strip() != "===CARD==="]

print(f"Anzahl gefundener Datenzeilen (ohne Trenner): {len(zeilen)}")

if len(zeilen) % 5 != 0:
    print("Achtung: Die Anzahl der Zeilen ist nicht durch 5 teilbar! Bitte prüfe deine Datei.")
else:
    print(f"Karten werden erkannt: {len(zeilen)//5}")
