.PHONY: fmt
fmt:
	black src/

.PHONY: lint
lint:
	pylint src/
