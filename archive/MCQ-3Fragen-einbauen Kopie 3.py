import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

# Datei blockweise lesen (3 Zeilen pro Karte, Leerzeile als Trenner)
with open(dateipfad, encoding="utf-8") as f:
    inhalt = f.read()

# Karten trennen anhand von Leerzeilen
blöcke_roh = inhalt.strip().split('\n\n')
blöcke = []

# Nur gültige Blöcke (genau 3 Zeilen) übernehmen
for block in blöcke_roh:
    zeilen = [zeile.strip() for zeile in block.strip().split('\n') if zeile.strip()]
    if len(zeilen) == 3:
        blöcke.append(zeilen)
    else:
        print(f"⚠️ Ungültiger Block gefunden (nicht exakt 3 Zeilen):\n{zeilen}\n")

anzahl_karten = len(blöcke)

print(f"\nEs wurden {anzahl_karten} gültige Karten erkannt.")

try:
    erwartete_karten = int(input("Wie viele Karten erwartest du? "))
except ValueError:
    print("❌ Ungültige Eingabe! Nur Zahlen erlaubt.")
    exit()

if erwartete_karten != anzahl_karten:
    print(f"❌ Erwartet: {erwartete_karten} Karten, aber gefunden: {anzahl_karten}")
    print("Bitte überprüfe die Textdatei (Antworten müssen in 3er-Blöcken mit Leerzeile getrennt stehen).")
    exit()

print("\n✅ Alles bereit. Bitte klicke in das erste Antwortfeld. Start in 15 Sekunden...")
time.sleep(15)

def eintrag_einfuegen(text):
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

# Einfügen aller Antwortoptionen je Karte
for k, antworten in enumerate(blöcke):
    pyautogui.press('tab')  # Tab zum 1. Feld
    time.sleep(0.2)
    pyautogui.press('tab')  # Tab zum 2. Feld
    time.sleep(0.2)
    time.sleep(1)           # kleine Sicherheitswartezeit
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('tab')

    for i in range(3):
        eintrag_einfuegen(antworten[i])
        if i < 2:
            pyautogui.press('tab')
            time.sleep(0.2)

    if k < anzahl_karten - 1:
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        print(f"✅ Karte {k + 1} eingefügt.")
    else:
        print("\n🎉 Alle Karten eingefügt!")

print("🚀 Vorgang abgeschlossen.")
