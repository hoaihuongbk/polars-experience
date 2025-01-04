SHELL := /bin/bash

init_venv:
	@echo "Initializing uv environment once"
	@brew install uv

run:
	@echo "Run the sample hello.py file"
	@uv run hello.py

clean:
	@echo "Clean up"
	@rm -Rf .venv uv.lock

