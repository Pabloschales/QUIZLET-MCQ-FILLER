
import os

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

print("---------- DEBUG CHECK ----------")
print("Script läuft in Verzeichnis:", os.getcwd())
print("Pfad zur Datei:", dateipfad)
print("Absoluter Pfad:", os.path.abspath(dateipfad))
print("Datei existiert?", os.path.exists(dateipfad))
print("Inhalt des Ordners:")
for f in os.listdir(os.path.dirname(dateipfad)):
    print(" -", f)
with open(dateipfad, encoding="utf-8") as f:
    lines = list(f)
print("Datei enthält (ALLE Zeilen, auch leer):", len(lines))
print("Erste 5 Zeilen der Datei:")
for i, line in enumerate(lines[:5], 1):
    print(f"{i}: {repr(line)}")
print("Letzte 5 Zeilen der Datei:")
for i, line in enumerate(lines[-5:], 1):
    print(f"{len(lines)-5+i}: {repr(line)}")
print("---------- END DEBUG ----------")
exit()

import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

# Alle nicht-leeren Zeilen einlesen
with open(dateipfad, encoding="utf-8") as f:
    antworten = [zeile.strip() for zeile in f if zeile.strip()]

gesamt = len(antworten)
if gesamt % 3 != 0:
    print(f"❗ Achtung: {gesamt} nicht-leere Zeilen – NICHT durch 3 teilbar!")
    print("Es werden nur die ersten vollen Dreierblöcke verarbeitet, Rest wird ignoriert.")

anzahl_karten = gesamt // 3
print(f"\n✅ Es werden {anzahl_karten} Karten verarbeitet.")

try:
    erwartete_karten = int(input("Wie viele Karten erwartest du? "))
except ValueError:
    print("❌ Ungültige Eingabe! Nur Zahlen erlaubt.")
    exit()

if erwartete_karten != anzahl_karten:
    print(f"❌ Erwartet: {erwartete_karten} Karten, aber gefunden: {anzahl_karten}")
    print("Bitte überprüfe die Textdatei (Antworten müssen in 3er-Blöcken stehen, ohne leere oder zusätzliche Zeilen).")
    exit()

print("\n✅ Alles bereit. Bitte klicke in das erste Antwortfeld. Start in 15 Sekunden...")
time.sleep(15)

def eintrag_einfuegen(text):
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

for k in range(anzahl_karten):
    antworten_block = antworten[k*3:(k+1)*3]

    pyautogui.press('tab')  # Tab zum 1. Feld
    time.sleep(0.2)
    pyautogui.press('tab')  # Tab zum 2. Feld
    time.sleep(1)
    pyautogui.press('enter')  # Öffnet Multiple-Choice-Feld
    time.sleep(0.3)
    pyautogui.press('tab')

    for i in range(3):
        eintrag_einfuegen(antworten_block[i])
        if i < 2:
            pyautogui.press('tab')
            time.sleep(0.2)

    if k < anzahl_karten - 1:
        pyautogui.press('tab')  # Zwischenbereich
        time.sleep(0.2)
        pyautogui.press('tab')  # Nächste Karte
        time.sleep(0.4)

print(f"\n🎉 Alle {anzahl_karten} Karten erfolgreich verarbeitet.")
