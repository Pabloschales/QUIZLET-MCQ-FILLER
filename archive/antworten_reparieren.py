# antworten_reparieren.py

EINGABE_DATEI = "antworten.txt"
AUSGABE_DATEI = "antworten_bereinigt.txt"

def lade_zeilen(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        return [zeile.strip() for zeile in f if zeile.strip()]

def repariere_und_gruppiere(zeilen):
    bereinigt = []
    block = []

    for zeile in zeilen:
        block.append(zeile)
        if len(block) == 3:
            bereinigt.append(block)
            block = []

    if block:
        print("⚠️ ACHTUNG: Unvollständiger Block erkannt und ignoriert:", block)

    return bereinigt

def speichere_bereinigt(bloecke, dateiname):
    with open(dateiname, "w", encoding="utf-8") as f:
        for block in bloecke:
            f.write("\n".join(block) + "\n")

def main():
    zeilen = lade_zeilen(EINGABE_DATEI)
    bloecke = repariere_und_gruppiere(zeilen)
    speichere_bereinigt(bloecke, AUSGABE_DATEI)
    print(f"✅ Fertig! {len(bloecke)} Dreierblöcke (=Karten) gespeichert.")
    input("✅ Drücke [Return] zum Beenden...")

if __name__ == "__main__":
    main()
