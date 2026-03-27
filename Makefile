.PHONY: run docker-up docker-down deploy

# Run the dashboard locally against upstream Datastore (read-only).
run:
	cd dashboard && uv run main.py

# Run both services locally via Docker Compose.
docker-up:
	docker compose up --build

# Stop and remove Docker containers.
docker-down:
	docker compose down

# Deploy all services to App Engine.
deploy:
	uv export --package tba-notification-firehose --format requirements-txt --no-hashes --no-dev -o dashboard/requirements.txt
	sed -i '' 's|-e ./shared|./shared|' dashboard/requirements.txt
	cp -r shared/ dashboard/shared/
	uv export --package tba-incoming --format requirements-txt --no-hashes --no-dev -o incoming/requirements.txt
	sed -i '' 's|-e ./shared|./shared|' incoming/requirements.txt
	cp -r shared/ incoming/shared/
	gcloud app deploy dashboard/app.yaml incoming/app.yaml dispatch.yaml --version=1 --quiet
	rm -rf dashboard/shared/ dashboard/requirements.txt incoming/shared/ incoming/requirements.txt
