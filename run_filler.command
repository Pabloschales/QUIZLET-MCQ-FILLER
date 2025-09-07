#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  echo "VENV fehlt. Bitte einmal scripts/setup_macos.command ausführen."
  exit 1
fi
source .venv/bin/activate
python3 QUIZLET-MCQ-FILLER.py
