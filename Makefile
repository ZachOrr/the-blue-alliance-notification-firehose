.PHONY: run dev build-dashboard deploy requirements

# Run the dashboard locally against upstream Datastore (read-only).
run:
	cd dashboard && uv run main.py

# Run the dashboard in development mode with hot reload.
# Starts Flask (port 8080) and the Vite dev server (port 5173) concurrently.
# Open http://localhost:5173 in your browser. Ctrl+C kills both servers.
dev:
	@trap 'kill 0' INT TERM; \
	(cd dashboard && uv run main.py) & \
	(cd dashboard/frontend && npm run dev) & \
	wait

# Build the React frontend for production (output to dashboard/static/build/).
build-dashboard:
	cd dashboard/frontend && npm run build

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
deploy: build-dashboard requirements
	cp -r shared/ dashboard/shared/
	cp -r shared/ incoming/shared/
	gcloud app deploy dashboard/app.yaml incoming/app.yaml dispatch.yaml --version=1 --quiet
	rm -rf dashboard/shared/ incoming/shared/
