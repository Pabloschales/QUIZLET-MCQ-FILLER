import pyautogui
import pyperclip
import time
import re

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

# Datei lesen
with open(dateipfad, encoding="utf-8") as f:
    inhalt = f.read()

# Robust trennen: auch \n\n\n oder \n \n \n wird korrekt erkannt
blöcke_roh = re.split(r'\n\s*\n', inhalt.strip())
blöcke = []

print(f"\n🔎 Debug: {len(blöcke_roh)} potenzielle Blöcke erkannt.")

# Nur gültige Blöcke mit genau 3 Zeilen übernehmen
for i, block in enumerate(blöcke_roh):
    zeilen = [zeile.strip() for zeile in block.strip().split('\n') if zeile.strip()]
    if len(zeilen) == 3:
        blöcke.append(zeilen)
    else:
        print(f"⚠️ Block {i + 1} enthält {len(zeilen)} Zeilen statt 3 und wird ignoriert:\n{zeilen}\n")

anzahl_karten = len(blöcke)

print(f"\n✅ Es wurden {anzahl_karten} gültige Karten erkannt.")

try:
    erwartete_karten = int(input("Wie viele Karten erwartest du? "))
except ValueError:
    print("❌ Ungültige Eingabe! Nur Zahlen erlaubt.")
    exit()

if erwartete_karten != anzahl_karten:
    print(f"❌ Erwartet: {erwartete_karten} Karten, aber gefunden: {anzahl_karten}")
    print("Bitte überprüfe die Textdatei (Antworten müssen in 3er-Blöcken mit Leerzeile dazwischen stehen).")
    exit()

print("\n✅ Alles bereit. Bitte klicke in das erste Antwortfeld. Start in 15 Sekunden...")
time.sleep(15)

def eintrag_einfuegen(text):
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

# Automatisches Einfügen in Quizlet
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
        print("\n🎉 Alle Karten erfolgreich eingefügt!")

print("🚀 Vorgang abgeschlossen.")
