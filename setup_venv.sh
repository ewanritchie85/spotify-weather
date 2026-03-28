#!/usr/bin/env bash
set -euo pipefail

# Creates a Python virtual environment in ./venv and installs requirements
PYTHON=${PYTHON:-python3}
VENV_DIR=${VENV_DIR:-venv}

echo "Creating virtual environment in ./${VENV_DIR} using ${PYTHON}..."
$PYTHON -m venv "$VENV_DIR"
echo "Activating venv and upgrading pip..."
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip setuptools wheel
if [ -f requirements.txt ]; then
  echo "Installing requirements.txt..."
  pip install -r requirements.txt
else
  echo "No requirements.txt found. You can add one and re-run this script."
fi

echo "Done. Activate with: source ${VENV_DIR}/bin/activate"
