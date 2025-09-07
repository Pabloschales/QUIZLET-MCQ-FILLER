import pyautogui
import pyperclip
import time
import subprocess
import json
import os

start = time.time()

# Timing-Parameter (4x Original)
# Original: SHORT=0.20, PASTE=0.35, TAB=0.20
T_SHORT = 0.80  # 4x 0.20
T_PASTE = 1.40  # 4x 0.35
T_TAB = 0.80    # 4x 0.20

# ✅ Safari aktivieren → erzeugt System-Sound beim Fokuswechsel
subprocess.call(["osascript", "-e", "tell application \"Safari\" to activate"])
time.sleep(1.0)

pfad = os.path.dirname(__file__)
dateipfad = os.path.join(pfad, "antworten.txt")
pos_path = os.path.join(pfad, "field_positions.json")

def calibrate_positions():
    print("Kalibrierung: Ich nehme die Positionen der 4 Optionsfelder per Mauszeiger auf.")
    print("Bitte bewege den Mauszeiger nacheinander auf: Option 1, Option 2, Option 3, Option 4.")
    positions = {}
    labels = ["term", "opt1", "opt2", "opt3", "opt4"]
    for label in labels:
        for sec in [3,2,1]:
            print(f"  {label}: Position wird in {sec}s aufgenommen…")
            time.sleep(1)
        x, y = pyautogui.position()
        positions[label] = {"x": x, "y": y}
        print(f"  {label}: gespeichert bei ({x}, {y})")
    with open(pos_path, "w", encoding="utf-8") as f:
        json.dump(positions, f)
    print("Kalibrierung abgeschlossen. Datei field_positions.json erstellt.")
    return positions

def load_positions():
    if os.path.exists(pos_path):
        try:
            with open(pos_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Falls 'term' fehlt, neu kalibrieren
                needed = {"term", "opt1", "opt2", "opt3", "opt4"}
                if not needed.issubset(set(data.keys())):
                    return calibrate_positions()
                return data
        except Exception:
            pass
    return calibrate_positions()

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
time.sleep(15)

positions = load_positions()

for k in range(anzahl_karten):
    basis = k * 5

    # Begriff
    if "term" in positions:
        pyautogui.click(positions["term"]["x"], positions["term"]["y"])  # Begriff-Feld fokussieren
        time.sleep(T_TAB)
    pyperclip.copy(zeilen[basis])
    time.sleep(T_SHORT)
    pyautogui.hotkey('command', 'v')
    time.sleep(T_PASTE)

    # Option 1
    pyautogui.click(positions["opt1"]["x"], positions["opt1"]["y"])  # fokussiere Option 1
    time.sleep(T_TAB)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(T_SHORT)
    pyautogui.hotkey('command', 'v')
    time.sleep(T_PASTE)

    # Option 2
    pyautogui.click(positions["opt2"]["x"], positions["opt2"]["y"])  # fokussiere Option 2
    time.sleep(T_TAB)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(T_SHORT)
    pyautogui.hotkey('command', 'v')
    time.sleep(T_PASTE)

    # Option 3
    pyautogui.click(positions["opt3"]["x"], positions["opt3"]["y"])  # fokussiere Option 3
    time.sleep(T_TAB)
    pyperclip.copy(zeilen[basis + 3])
    time.sleep(T_SHORT)
    pyautogui.hotkey('command', 'v')
    time.sleep(T_PASTE)

    # Option 4
    pyautogui.click(positions["opt4"]["x"], positions["opt4"]["y"])  # fokussiere Option 4
    time.sleep(T_TAB)
    pyperclip.copy(zeilen[basis + 4])
    time.sleep(T_SHORT)
    pyautogui.hotkey('command', 'v')
    time.sleep(T_PASTE)

    if k < anzahl_karten - 1:
        pyautogui.press('tab')
        time.sleep(T_TAB)
        pyautogui.press('tab')
        time.sleep(T_TAB)
        print(f"Karte {k + 1} fertig, nächste Karte wird bearbeitet...")
    else:
        print("Alle Karten wurden erfolgreich ausgefüllt!")

print("Vorgang abgeschlossen.")
end = time.time()
print(f"Gesamtdauer: {end - start:.2f} Sekunden")

# 🔊 Hero Sound als Abschluss (fehlertolerant)
try:
    subprocess.call(["afplay", "/System/Library/Sounds/Hero.aiff"])  # kann auf manchen Systemen fehlschlagen
except Exception as e:
    pass
