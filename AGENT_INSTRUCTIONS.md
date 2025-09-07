# Agenten-Anleitung (macOS)

Ziel: Repo klonen/aktualisieren, Umgebung einrichten, Filler/Checker starten und Validierung durchführen. Kurz, deterministisch, mit klaren Erfolgs-/Fehlerkriterien.

## Voraussetzungen

- GUI-Session aktiv (pyautogui benötigt Desktop, kein reines SSH-Headless).
- Internetzugang zu github.com.
- Datei `antworten.txt` liegt im Projektroot und ist korrekt formatiert (siehe Format unten).

## Repository beziehen/aktualisieren

- Neu klonen (HTTPS):

```bash
git clone https://github.com/Pabloschales/QUIZLET-MCQ-FILLER.git
cd QUIZLET-MCQ-FILLER
```

- Aktualisieren:

```bash
cd QUIZLET-MCQ-FILLER
git pull --ff-only
```

## Setup (macOS)

```bash
chmod +x scripts/setup_macos.command run_filler.command run_checker.command
./scripts/setup_macos.command
```

Erwartung: `.venv/` wird erstellt; `pip install -r requirements.txt` erfolgreich.

## Start

- Filler starten (füllt Karten aus `antworten.txt` ein):

```bash
./run_filler.command
```

- Checker starten (liest Felder und vergleicht ab Karte 2):

```bash
./run_checker.command
```

## Ablauf (Operator-Hinweise)

1) Browser öffnen (macOS: Safari) und Quizlet-Eingabemaske öffnen.
2) In das erste „BEGRIFF“-Feld klicken.
3) Filler starten; 15s Countdown abwarten.
4) Nach dem Filler den Checker starten; 15s Countdown abwarten.
5) Ergebnis in `CHECK.txt` prüfen.

## Format von `antworten.txt`

Blöcke mit `===CARD===` als Trenner. Pro Karte 5 Zeilen: Begriff + 4 Optionen.

```text
===CARD===
Frage oder Begriff
Antwort A
Antwort B
Antwort C
Antwort D
```

Der Checker ignoriert Karte 1 und vergleicht ab Karte 2.

## Erfolgs-/Fehlerkriterien

- Erfolg Filler: Konsolenausgabe „Alle Karten wurden erfolgreich ausgefüllt!“.
- Erfolg Checker: Konsole meldet „Alle Karten ab Karte 2 stimmen exakt überein.“ und `CHECK.txt` enthält keine Unterschiede.
- Fehlerfälle und Maßnahmen:
  - Keine GUI/kein Fokus: Browser manuell aktivieren; Feld fokussieren; erneut starten.
  - Rechte fehlen (macOS): Systemeinstellungen > Datenschutz & Sicherheit:
    - Bedienungshilfen: Terminal/VS Code und `.venv`-Python erlauben.
    - Bildschirmaufnahme: Terminal/VS Code erlauben.
  - Langsame Ladezeiten: Delays im Code erhöhen (Tab/Enter/Copy-Pause).
  - `antworten.txt` fehlerhaft: Format prüfen, leere Zeilen und Trenner korrekt setzen.

## Wartung

- Abhängigkeiten aktualisieren:

```bash
source .venv/bin/activate
pip install -r requirements.txt --upgrade
```

- Lokale Änderungen committen/pushen (optional):

```bash
git add -A && git commit -m "Update" && git push
```

## Sicherheit/Compliance

- Automatisierung nur im Rahmen der Quizlet-Nutzungsbedingungen.
- Keine Zugangsdaten in das Repo schreiben.
