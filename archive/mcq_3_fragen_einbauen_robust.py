import os
import pyautogui
import pyperclip
import time

# Pfad zur Antworten-Datei im gleichen Verzeichnis wie dieses Skript
def get_answer_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'antworten.txt')

# Funktion zum Einfügen eines Textes in das aktive Feld
def eintrag_einfuegen(text):
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')  # Auf macOS ggf. 'command'
    time.sleep(0.2)

# Hauptfunktion zum Verarbeiten der Antworten
if __name__ == '__main__':
    dateipfad = get_answer_file_path()

    # Einlesen aller nicht-leeren Zeilen als Antworten
    with open(dateipfad, encoding='utf-8') as f:
        antworten = [zeile.strip() for zeile in f if zeile.strip()]

    # Prüfung auf Dreierblöcke
    gesamt = len(antworten)
    if gesamt % 3 != 0:
        print(f"❗ Achtung: {gesamt} nicht-leere Zeilen – nicht durch 3 teilbar. Rest wird ignoriert.")

    # Anzahl der Karten (volle Dreierblöcke)
    anzahl_karten = gesamt // 3
    print(f"\n✅ Es werden {anzahl_karten} Karten verarbeitet.")
    print("Bitte klicke in das erste Antwortfeld. Start in 15 Sekunden...")
    time.sleep(15)

    # Verarbeitung der Karten
    for k in range(anzahl_karten):
        block = antworten[k*3:(k+1)*3]
        for i, text in enumerate(block):
            eintrag_einfuegen(text)
            if i < 2:
                pyautogui.press('tab')
                time.sleep(0.2)

        # Tabben zur nächsten Karte (zwischen zwei weiteren Tabs)
        if k < anzahl_karten - 1:
            pyautogui.press('tab')
            time.sleep(0.2)
            pyautogui.press('tab')
            time.sleep(0.4)

    print(f"\n🎉 Alle {anzahl_karten} Karten erfolgreich verarbeitet.")
