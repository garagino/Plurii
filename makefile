# Makefile

VENV_NAME = venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
UVICORN = $(VENV_NAME)/bin/uvicorn

.PHONY: all
all: install

.PHONY: venv
venv:
	python3 -m venv $(VENV_NAME)

.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

.PHONY: run
run: install
	$(UVICORN) app.main:app --host localhost --port 8000 --reload

.PHONY: clean
clean:
	rm -rf $(VENV_NAME) __pycache__

.PHONY: activatevenv
activatevenv: venv
	source $(VENV_NAME)/scripts/activate

.PHONY: deactivatevenv
deactivatevenv:
	deactivate

.PHONY: help
help:
	@echo "make venv - create a virtual environment"
	@echo "make install - install dependencies"
	@echo "make run - run the FastAPI application"
	@echo "make clean - clean up temporary files"

