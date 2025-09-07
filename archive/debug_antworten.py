
import re

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

with open(dateipfad, encoding="utf-8") as f:
    inhalt = f.read()

blöcke_roh = re.split(r"
\s*
", inhalt.strip())

print(f"
🔍 Gesamtzahl erkannter Blöcke: {len(blöcke_roh)}
")

fehlerhafte_bloecke = []

for i, block in enumerate(blöcke_roh):
    zeilen = [zeile for zeile in block.strip().split("
") if zeile.strip()]
    if len(zeilen) != 3:
        print(f"⚠️ Block {i+1} hat {len(zeilen)} Zeilen:")
        for j, z in enumerate(zeilen, 1):
            print(f"  Zeile {j}: {repr(z)}")
        print("---\n")
        fehlerhafte_bloecke.append(i + 1)

anzahl_gueltig = len(blöcke_roh) - len(fehlerhafte_bloecke)
print(f"✅ Anzahl gültiger Blöcke mit exakt 3 Zeilen: {anzahl_gueltig}")
print(f"❌ Fehlerhafte Blöcke: {len(fehlerhafte_bloecke)} → {fehlerhafte_bloecke}")

