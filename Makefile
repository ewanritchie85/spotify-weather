VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# 1. Create the environment
env:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "----------------------------------------------------------"
	@echo "DONE. To activate, you must run: source $(VENV)/bin/activate"
	@echo "----------------------------------------------------------"

# 2. Install/Update pip and requirements
requirements:
	@echo "Installing requirements..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt


help:
	@echo "Usage:"
	@echo "  make setup    - Create venv and install requirements"
	@echo "  make clean    - Remove venv and temp files"