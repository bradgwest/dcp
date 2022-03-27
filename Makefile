.PHONY: format
format:
	black .
	isort .

.PHONY: qa
qa:
	black --check .
	isort --check .
	pylint
	flake8
