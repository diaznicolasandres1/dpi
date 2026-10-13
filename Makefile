PYTHON ?= python3

.PHONY: hub-update hub-update-changed hub-check new-submission

hub-update:
	$(PYTHON) scripts/update_hub.py

hub-update-changed:
	$(PYTHON) scripts/update_hub.py --changed-only

hub-check:
	$(PYTHON) scripts/check_hub.py

new-submission:
	@test -n "$(N)" || (echo "Usage: make new-submission N=4" && exit 1)
	$(PYTHON) scripts/new_submission.py $(N)
