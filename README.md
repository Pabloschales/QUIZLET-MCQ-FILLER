# Quizlet MCQ Filler + Checker (macOS)

Automatisiert das Ausfüllen von Quizlet-MCQ-Karten aus `antworten.txt` und prüft anschließend die Eingaben.

## Dateien

- `QUIZLET-MCQ-FILLER.py`: Fügt Karten automatisch ein (Clipboard + Tastaturnavigation)
- `CHECKER.py`: Liest Felder in Quizlet aus und vergleicht sie mit `antworten.txt` (ab Karte 2)
- `antworten.txt`: Quelle der Karten. Struktur siehe unten
- `CHECK.txt`: Ergebnisprotokoll des Checkers
- `MQC-FILLER-STARTER.command`: Startet den Filler auf macOS
- `MCQ-CHECKER.command`: Startet den Checker auf macOS
- `scripts/setup_macos.command`: Einmalige Einrichtung (venv + pip install)
- `run_filler.command` / `run_checker.command`: Starten Filler/Checker aus dem Projektverzeichnis

## Format von `antworten.txt`

Blöcke mit `===CARD===` als Trenner. Pro Karte 5 Zeilen: Begriff + 4 Antwortoptionen.

```text
===CARD===
Frage oder Begriff
Antwort A
Antwort B
Antwort C
Antwort D

===CARD===
...
```

Hinweis: Der Checker ignoriert Karte 1 absichtlich und vergleicht ab Karte 2.

## Voraussetzungen

- macOS (Safari wird per AppleScript fokussiert)
- Python 3.9+
- Zugriffe in Systemeinstellungen erlauben: Bedienungshilfen (Accessibility) für Terminal/Python/VS Code

Installiere Abhängigkeiten:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Nutzung

1) Öffne in Safari die Quizlet-Maske zum Erstellen von Karten und klicke in das erste BEGRIFF-Feld.
2) Fülle aus:
   - Doppelklick auf `MQC-FILLER-STARTER.command` oder Terminal: `./run_filler.command` (Start in 15s)
3) Prüfe:
   - Doppelklick auf `MCQ-CHECKER.command` oder Terminal: `./run_checker.command` (Start in 15s)

Beide Skripte spielen einen System-Sound bei Start/Ende. Der Filler nutzt feste Delays (Tabs/Enter). Passe Delays an, falls Felder zu langsam laden.

## Repo & VM-Setup

### Dieses Projekt als Git-Repository veröffentlichen

```bash
cd "/Users/pabloschales/Desktop/QUIZLET-MCQ-FILLER(+CHECKER)"
git init -b main
git add .
git commit -m "Initial commit"
# Erstelle ein leeres Repo bei GitHub und füge als origin hinzu
# SSH (empfohlen):
# git remote add origin git@github.com:<USER>/<REPO>.git
# HTTPS:
# git remote add origin https://github.com/<USER>/<REPO>.git
git push -u origin main
```

`.gitignore` enthält u. a.: `.venv/`, `__pycache__/`, `*.pyc`, `.DS_Store`, `.vscode/`.

### Klonen auf der VM (User: pelion)

```bash
# Git installieren (Linux) und SSH-Key hinterlegen
sudo apt update && sudo apt install -y git
ssh-keygen -t ed25519 -C "pelion@vm"
cat ~/.ssh/id_ed25519.pub  # in GitHub SSH Keys eintragen
ssh -T git@github.com

cd /home/pelion
git clone git@github.com:<USER>/<REPO>.git QUIZLET-MCQ-FILLER
cd QUIZLET-MCQ-FILLER
```

### macOS-Setup per Skript (Host oder macOS-VM)

```bash
chmod +x scripts/setup_macos.command run_filler.command run_checker.command
./scripts/setup_macos.command
```

Start:

```bash
./run_filler.command
./run_checker.command
```

## Typische Stolpersteine

- Ordnername enthält Klammern: .command-Skripte wurden auf den exakten Pfad angepasst.
- Safari nicht aktiv: Skripte aktivieren Safari automatisch.
- Clipboard leer oder falsche Auswahl: Checker kopiert mehrfach mit Retry-Logik.

## Haftung

Dieses Projekt ist ein praktisches Automationsskript. Nutze es verantwortungsvoll und beachte die Nutzungsbedingungen von Quizlet.
