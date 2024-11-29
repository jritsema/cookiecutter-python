all: help

.PHONY: help
help: Makefile
	@echo
	@echo " Choose a make command to run"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo

## install: install project dependencies
.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip freeze > piplock.txt

## start: run local project
.PHONY: start
start:
	clear
	@echo ""
	python -u main.py

