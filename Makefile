run: launch                         ## Launch the mission
test: fill_tanks systems_check      ## Run tests
install:                            ## Install dependencies

launch:
	@echo Starting engines ...
	python -m mission.mission

systems_check:
	@echo Systems check ...
	pytest

fill_tanks:
	@echo Filling up tanks ...
	pip install -r requirements.txt

help:                       ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help