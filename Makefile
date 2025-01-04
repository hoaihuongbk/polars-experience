SHELL := /bin/bash

init_venv:
	@echo "Initializing uv environment once"
	@brew install uv

run:
	@echo "Run the sample hello.py file"
	@uv run hello.py

run_delta:
	@echo "Run the sample hello_delta.py file"
	@uv run hello_delta.py

run_iceberg:
	@echo "Run the sample hello_iceberg.py file"
	@uv run hello_iceberg.py

run_duckdb:
	@echo "Run the sample hello_duckdb.py file"
	@uv run hello_duckdb.py

clean:
	@echo "Clean up"
	@rm -Rf .venv uv.lock

