# Makefile for the project

.PHONY: install run clean

# Install project dependencies
install:
	@echo "Installing dependencies..."
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements.txt

# Run the main script
run:
	@echo "Running the main script..."
	.venv/bin/python3 src/main.py

# Run tests
# Disabled at the moment
#test:
#	@echo "Running tests..."
#	pytest
#
## Lint the project using flake8
#lint:
#	@echo "Linting the project..."
#	flake8 .

# Clean the project
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
