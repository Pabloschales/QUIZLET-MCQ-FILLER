import pyautogui
import pyperclip
import time
import os
import sys
import subprocess
import json

# ✅ Browser aktivieren
subprocess.call(["osascript", "-e", 'tell application "Safari" to activate'])
time.sleep(1.0)

# 📁 Pfade
pfad = os.path.dirname(__file__)
antworten_path = os.path.join(pfad, "antworten.txt")
check_path = os.path.join(pfad, "CHECK.txt")
pos_path = os.path.join(pfad, "field_positions.json")

# Kalibrierung der Felder (gleich wie im Filler)
def calibrate_positions():
    print("Kalibrierung: Ich nehme die Positionen für Begriff + 4 Optionen per Mauszeiger auf.")
    print("Bitte bewege den Mauszeiger nacheinander auf: Begriff, Option 1, Option 2, Option 3, Option 4.")
    positions = {}
    labels = ["term", "opt1", "opt2", "opt3", "opt4"]
    for label in labels:
        for sec in [3, 2, 1]:
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
                needed = {"term", "opt1", "opt2", "opt3", "opt4"}
                if not needed.issubset(set(data.keys())):
                    return calibrate_positions()
                return data
        except Exception:
            pass
    return calibrate_positions()

# 🧾 antworten.txt einlesen
if not os.path.exists(antworten_path):
    print("❌ antworten.txt nicht gefunden.")
    sys.exit()

with open(antworten_path, encoding="utf-8") as f:
    original_lines = [line.strip() for line in f if line.strip()]

# Blöcke (Karten) extrahieren
original_blocks = []
block = []
for line in original_lines:
    if line == "===CARD===":
        if block:
            original_blocks.append(block)
        block = []
    else:
        block.append(line)
if block:
    original_blocks.append(block)

# 👇 Karte 1 ignorieren
original_blocks = original_blocks[1:]
anzahl_karten = len(original_blocks)

print(f"▶️ {anzahl_karten} Karten (ab Karte 2) werden überprüft.")
print("👉 Klicke in das erste Feld in Quizlet. Start in 15 Sekunden...")
time.sleep(15)

positions = load_positions()

pyperclip.copy("")

# Daten sammeln
copied_blocks = []
labels = ["term", "opt1", "opt2", "opt3", "opt4"]
for k in range(anzahl_karten + 1):  # inkl. Karte 1
    block = []
    for i, lab in enumerate(labels):
        # Fokussiere das entsprechende Feld mit einem Klick
        coords = positions.get(lab)
        if coords:
            pyautogui.click(coords["x"], coords["y"])
            time.sleep(0.80)
        # Inhalt kopieren
        pyautogui.hotkey('command', 'a')
        time.sleep(0.80)
        pyautogui.hotkey('command', 'c')
        time.sleep(1.40)
        text = pyperclip.paste().strip()

        retry = 0
        while (not text or len(text) > 200 or "import pyautogui" in text) and retry < 5:
            time.sleep(1.40)
            pyautogui.hotkey('command', 'c')
            time.sleep(1.40)
            text = pyperclip.paste().strip()
            retry += 1

        block.append(text)

    copied_blocks.append(block)

    # Kartenwechsel (Tab, Tab) bleibt erhalten – wirkt außerhalb der Optionsfelder
    if k < anzahl_karten:
        pyautogui.press('tab')
        time.sleep(0.80)
        pyautogui.press('tab')
        time.sleep(0.80)

# ❌ Karte 1 rausnehmen
copied_blocks = copied_blocks[1:]

# CHECK.txt schreiben
with open(check_path, "w", encoding="utf-8") as f:
    for block in copied_blocks:
        f.write("===CARD===\n")
        for line in block:
            f.write(line + "\n")
        f.write("\n")

    # Vergleich durchführen
    abweichungen = []
    for i, (orig, check) in enumerate(zip(original_blocks, copied_blocks), start=2):
        if orig != check:
            abweichungen.append(i)

    f.write("\n")
    if abweichungen:
        f.write("❌ Unterschiede bei folgenden Karten:\n")
        f.write(", ".join(map(str, abweichungen)) + "\n")
    else:
        f.write("✅ Alle Karten ab Karte 2 stimmen exakt überein.\n")

# Terminal-Ausgabe
print("\n=== Vergleich abgeschlossen ===")
if abweichungen:
    print("❌ Unterschiede bei Karten:", ", ".join(map(str, abweichungen)))
else:
    print("🎉 Alle Karten ab Karte 2 stimmen exakt überein.")
print("📁 Ergebnis steht in CHECK.txt")

# 🔊 Endton abspielen
try:
    subprocess.call(["afplay", "/System/Library/Sounds/Hero.aiff"])  # kann fehlschlagen
except Exception:
    pass
