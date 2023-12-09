.PHONY: fmt
fmt:
	black src/

.PHONY: lint
lint:
	pylint $$(git ls-files '*.py')
