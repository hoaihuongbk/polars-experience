SHELL := /bin/bash

init_venv:
	@echo "Initializing uv environment once"
	@brew install uv

run:
	@if [ -n "$(TEST)" ]; then \
		echo "Running hello_$(TEST).py"; \
		uv run hello_$(TEST).py; \
	else \
		echo "Running hello.py"; \
		uv run hello.py; \
	fi

clean:
	@echo "Clean up"
	@rm -Rf .venv uv.lock

