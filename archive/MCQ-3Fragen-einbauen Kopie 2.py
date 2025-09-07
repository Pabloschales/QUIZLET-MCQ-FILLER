import pyautogui
import pyperclip
import time

dateipfad = "/Users/pabloschales/Python/MeinProjekt/antworten.txt"

with open(dateipfad, encoding="utf-8") as f:
    zeilen = [line.strip() for line in f if line.strip()]

anzahl_zeilen = len(zeilen)

print("Wieviele Karten (Fragen) soll das Set enthalten?")
try:
    erwartete_karten = int(input("Bitte gib die erwartete Anzahl an Karten (Fragen) ein: "))
except ValueError:
    print("Ungültige Eingabe! Bitte nur eine Zahl eingeben.")
    exit()

if anzahl_zeilen % 3 != 0:
    print(f"Achtung! Die Zeilenzahl ({anzahl_zeilen}) ist nicht durch 3 teilbar. Jede Karte braucht exakt 3 Zeilen!")
    exit()

berechnete_karten = anzahl_zeilen // 3

if erwartete_karten != berechnete_karten:
    print(f"Achtung! Deine Eingabe ({erwartete_karten} Karten) stimmt nicht mit der Anzahl in der Datei ({berechnete_karten} Karten) überein!")
    print("Bitte prüfe deine Datei!")
    exit()

print(f"\nAlles ok: {berechnete_karten} Karten werden eingefügt.")
print("Klicke jetzt in das erste 'FRAGE'-Feld. Start in 15 Sekunden...")
time.sleep(15)

for k in range(berechnete_karten):
    basis = k * 3
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.2)

    pyperclip.copy(zeilen[basis])
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

    pyautogui.press('tab')
    time.sleep(0.2)
    pyperclip.copy(zeilen[basis + 1])
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

    pyautogui.press('tab')
    time.sleep(0.2)
    pyperclip.copy(zeilen[basis + 2])
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.3)

    if k < berechnete_karten - 1:
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        print(f"Karte {k + 1} fertig, nächste Karte wird bearbeitet...")
    else:
        print("Alle Karten wurden erfolgreich ausgefüllt!")

print("Vorgang abgeschlossen.")
