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

## install: add a new package (make install <package>), or install all project dependencies from piplock.txt (make install)
.PHONY: install
install:
	python -m pip install --upgrade pip
ifeq ($(filter-out $@,$(MAKECMDGOALS)),)
	@echo "Installing dependencies from piplock.txt"
	pip install -r piplock.txt
else
	@echo "Adding package $(filter-out $@,$(MAKECMDGOALS)) to requirements.txt"
	@grep -q "^$(filter-out $@,$(MAKECMDGOALS))$$" requirements.txt || echo "$(filter-out $@,$(MAKECMDGOALS))" >> requirements.txt
	pip install $(filter-out $@,$(MAKECMDGOALS))
	pip install -r requirements.txt
	pip freeze > piplock.txt
endif

# Empty rule to handle package name argument
%:
	@:

## start: run local project
.PHONY: start
start:
	clear
	@echo ""
	python -u main.py
