help:
	@echo "run"
	@echo "test"
	@echo "install"
	@echo "black"
	@echo "pylint"
test:
	pytest --cov=src --cov-config=.coveragerc --cov-report=html
run:
	uvicorn src.main:app
install:
	pip install -r requirements.txt
black:
	black src
	pylint src