import pyautogui
import pyperclip
import time

dateipfad = "antworten.txt"

# Datei einlesen und Trenner entfernen
with open(dateipfad, encoding="utf-8") as f:
    zeilen = [line.strip() for line in f if line.strip() and line.strip() != "===CARD==="]

anzahl_karten = len(zeilen) // 5

print(f"Anzahl gefundener Datenzeilen (ohne Trenner): {len(zeilen)}")
if len(zeilen) % 5 != 0:
    print("Achtung: Die Anzahl der Zeilen ist nicht durch 5 teilbar! Bitte prüfe deine Datei.")
    exit()
else:
    print(f"Karten werden erkannt: {anzahl_karten}")

print("Klicke jetzt ins erste FRAGE-Feld und lasse den Cursor dort blinken.")
print("Das Script startet automatisch in 10 Sekunden!")
time.sleep(10)

for k in range(anzahl_karten):
    basis = k * 5

    # Fragefeld füllen (Clipboard doppelt, für Mac/Safari-Sicherheit)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyperclip.copy(zeilen[basis])
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis])
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.6)

    # Tab zu Antwortfeld, füllen
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.6)

    # Tab zu MCQ-Button und Enter
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.6)

    # Tab zu MCQ1, füllen
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.6)

    # Tab zu MCQ2, füllen
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyperclip.copy(zeilen[basis + 3])
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 3])
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.6)

    # Tab zu MCQ3, füllen
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyperclip.copy(zeilen[basis + 4])
    time.sleep(0.3)
    pyperclip.copy(zeilen[basis + 4])
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.6)

    # Zwei Mal Tab zum nächsten Fragefeld
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)

    print(f"Karte {k+1} fertig.")

print("Alle Karten wurden eingefügt!")
