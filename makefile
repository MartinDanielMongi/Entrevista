help:
	@echo "run"
	@echo "test"
	@echo "install"
	@echo "lint"
test:
	pytest --cov=. --cov-config=.coveragerc --cov-report=html
run:
	uvicorn src.main:app
install:
	pip install -r requirements.txt
lint:
	black src
	pylint src