import pyautogui
import pyperclip
import time

start = time.time()  # Startzeit für Zeitmessung

dateipfad = "antworten.txt"

with open(dateipfad, encoding="utf-8") as f:
    zeilen = [
        line.strip()
        for line in f
        if line.strip() and line.strip() != "===CARD==="
    ]

anzahl_karten = len(zeilen) // 5

if len(zeilen) % 5 != 0:
    print(f"Achtung! Deine Datei enthält {len(zeilen)} relevante Zeilen – das sind {len(zeilen)//5} komplette Karten. Es bleiben {len(zeilen)%5} Zeilen übrig, die ignoriert werden!")

if anzahl_karten == 0:
    print("Keine Karten gefunden! Mindestens 5 Zeilen werden benötigt.")
    exit()

print(f"Starte automatisch: {anzahl_karten} Karten werden eingefügt. Klicke in das erste 'BEGRIFF'-Feld. Start in 15 Sekunden...")
time.sleep(15)   # Startzeit bleibt gleich

for k in range(anzahl_karten):
    basis = k * 5

    # Frage/Begriff (Feld 1)
    pyperclip.copy(zeilen[basis])
    time.sleep(0.11)  # war 0.10
    pyautogui.hotkey('command', 'v')
    time.sleep(0.275)  # war 0.25

    # Tab zu Definition (richtige Antwort)
    pyautogui.press('tab')
    time.sleep(0.11)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.11)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.275)

    # Tab zu MCQ-Button (öffnet die 3 Felder für falsche Antworten)
    pyautogui.press('tab')
    time.sleep(0.11)
    pyautogui.press('enter')
    time.sleep(0.275)

    # Tab zu MCQ-Option 1
    pyautogui.press('tab')
    time.sleep(0.11)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.11)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.275)

    # Tab zu MCQ-Option 2
    pyautogui.press('tab')
    time.sleep(0.11)
    pyperclip.copy(zeilen[basis + 3])
    time.sleep(0.11)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.275)

    # Tab zu MCQ-Option 3
    pyautogui.press('tab')
    time.sleep(0.11)
    pyperclip.copy(zeilen[basis + 4])
    time.sleep(0.11)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.275)

    # Tab zur nächsten Karte (zweimal Tab)
    if k < anzahl_karten - 1:
        pyautogui.press('tab')
        time.sleep(0.11)
        pyautogui.press('tab')
        time.sleep(0.11)
        print(f"Karte {k + 1} fertig, nächste Karte wird bearbeitet...")
    else:
        print("Alle Karten wurden erfolgreich ausgefüllt!")

print("Vorgang abgeschlossen.")

end = time.time()
print(f"Gesamtdauer: {end - start:.2f} Sekunden")
