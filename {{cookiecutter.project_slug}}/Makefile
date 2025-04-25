all: help

.PHONY: help
help: Makefile
	@echo
	@echo " Choose a make command to run"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo

## init: initialize a new python project
.PHONY: init
init:
	python -m venv .venv
	direnv allow .
	type python

## piplock: installs dependencies in requirements.txt and generates piplock.txt
.PHONY: piplock
piplock:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip freeze > piplock.txt

## install: install project dependencies from piplock.txt
.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install -r piplock.txt

## start: run local project
.PHONY: start
start:
	clear
	@echo ""
	python -u main.py
