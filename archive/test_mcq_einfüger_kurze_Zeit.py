import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

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
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    time.sleep(1)  # Enter-Wartezeit lassen wir hier bewusst etwas länger
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.2)

    pyperclip.copy(zeilen[basis])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.3)

    pyautogui.press('tab')
    time.sleep(0.2)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.3)

    pyautogui.press('tab')
    time.sleep(0.2)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.2)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    time.sleep(0.3)

    if k < anzahl_karten - 1:
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        print(f"Karte {k + 1} fertig, nächste Karte wird bearbeitet...")
    else:
        print("Alle Karten wurden erfolgreich ausgefüllt!")

print("Vorgang abgeschlossen.")
