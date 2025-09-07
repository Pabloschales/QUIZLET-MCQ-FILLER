import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

# Lies die ersten 3 Zeilen ein
with open(dateipfad, encoding="utf-8") as f:
    zeilen = [line.strip() for line in f if line.strip()]

if len(zeilen) < 3:
    print("Es müssen mindestens 3 Zeilen in der Datei stehen!")
    exit()

print("Klicke jetzt ins Feld 'FRAGE' (ganz oben, nicht 'Antwort')! Start in 5 Sekunden...")
time.sleep(5)

# 1. Tab zu 'Antwort'
pyautogui.press('tab')
time.sleep(0.3)
# 2. Tab zum Button "Optionen für Multiple Choice-Fragen hinzufügen"
pyautogui.press('tab')
time.sleep(0.3)
# 1 Sekunde warten
time.sleep(1)
# Enter, um die 3 Zeilen zu öffnen
pyautogui.press('enter')
time.sleep(0.5)
# Tab zu "Option 1"
pyautogui.press('tab')
time.sleep(0.3)

# Erste Zeile einfügen
pyperclip.copy(zeilen[0])
time.sleep(0.2)
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(0.5)

# Tab zu "Option 2"
pyautogui.press('tab')
time.sleep(0.3)
pyperclip.copy(zeilen[1])
time.sleep(0.2)
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(0.5)

# Tab zu "Option 3"
pyautogui.press('tab')
time.sleep(0.3)
pyperclip.copy(zeilen[2])
time.sleep(0.2)
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(0.5)

print("FERTIG! Alle drei Optionen eingefügt.")
