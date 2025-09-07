import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

# Datei lesen und Zeilen filtern
with open(dateipfad, encoding="utf-8") as f:
    zeilen = [line.strip() for line in f if line.strip()]

anzahl_karten = len(zeilen) // 3

if anzahl_karten == 0:
    print("Keine Karten gefunden! Mindestens 3 Zeilen werden benötigt.")
    exit()

print(f"Starte automatisch: {anzahl_karten} Karten werden eingefügt. Klicke in das erste 'FRAGE'-Feld. Start in 5 Sekunden...")
time.sleep(5)

for k in range(anzahl_karten):
    basis = k * 3
    # 1. Tab zu 'Antwort'
    pyautogui.press('tab')
    time.sleep(0.3)
    # 2. Tab zum Button "Optionen für Multiple Choice-Fragen hinzufügen"
    pyautogui.press('tab')
    time.sleep(0.3)
    time.sleep(1)
    # Enter, um die 3 Zeilen zu öffnen
    pyautogui.press('enter')
    time.sleep(0.5)
    # Tab zu "Option 1"
    pyautogui.press('tab')
    time.sleep(0.3)

    # 1. Antwort einfügen
    pyperclip.copy(zeilen[basis])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.5)

    # Tab zu Option 2 und einfügen
    pyautogui.press('tab')
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.5)

    # Tab zu Option 3 und einfügen
    pyautogui.press('tab')
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.5)

    # 2x Tab zur nächsten Karte (außer letzte Karte)
    if k < anzahl_karten - 1:
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('tab')
        time.sleep(0.3)
        print(f"Karte {k + 1} fertig, nächste Karte wird bearbeitet...")
    else:
        print("Alle Karten wurden erfolgreich ausgefüllt!")

print("Vorgang abgeschlossen.")
