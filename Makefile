.PHONY: run deploy requirements

# Run the dashboard locally against upstream Datastore (read-only).
run:
	cd dashboard && uv run main.py

# Generate requirements.txt for each service from uv workspace.
# Works on both macOS and Linux (uses perl for portable in-place editing).
requirements:
	@for spec in "tba-notification-firehose:dashboard" "tba-incoming:incoming"; do \
		pkg=$${spec%%:*}; dir=$${spec##*:}; \
		uv export --package "$$pkg" --format requirements-txt --no-hashes --no-dev \
			-o "$$dir/requirements.txt"; \
		perl -pi -e 's/^-e \.\/shared/.\/shared/' "$$dir/requirements.txt"; \
	done

# Deploy all services to App Engine.
deploy: requirements
	cp -r shared/ dashboard/shared/
	cp -r shared/ incoming/shared/
	gcloud app deploy dashboard/app.yaml incoming/app.yaml dispatch.yaml --version=1 --quiet
	rm -rf dashboard/shared/ incoming/shared/
