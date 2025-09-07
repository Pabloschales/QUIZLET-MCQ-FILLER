import pyautogui
import pyperclip
import time
import os
import sys
import subprocess

# ✅ Browser aktivieren
subprocess.call(["osascript", "-e", 'tell application "Safari" to activate'])

# 📁 Pfade
pfad = os.path.dirname(__file__)
antworten_path = os.path.join(pfad, "antworten.txt")
check_path = os.path.join(pfad, "CHECK.txt")

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

pyperclip.copy("")

# Daten sammeln
copied_blocks = []
for k in range(anzahl_karten + 1):  # inkl. Karte 1
    block = []
    for i in range(5):
        pyautogui.hotkey('command', 'a')
        time.sleep(0.2)
        pyautogui.hotkey('command', 'c')
        time.sleep(0.5)
        text = pyperclip.paste().strip()

        retry = 0
        while (not text or len(text) > 200 or "import pyautogui" in text) and retry < 3:
            time.sleep(0.5)
            pyautogui.hotkey('command', 'c')
            time.sleep(0.5)
            text = pyperclip.paste().strip()
            retry += 1

        block.append(text)

        if i < 4:
            pyautogui.press('tab')
            time.sleep(0.2)

    copied_blocks.append(block)

    if k < anzahl_karten:
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)

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
subprocess.call(["afplay", "/System/Library/Sounds/Hero.aiff"])
