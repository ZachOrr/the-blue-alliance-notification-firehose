.PHONY: run docker-up docker-down

# Run the dashboard locally against upstream Datastore (read-only).
run:
	cd dashboard && uv run main.py

# Run both services locally via Docker Compose.
docker-up:
	docker compose up --build

# Stop and remove Docker containers.
docker-down:
	docker compose down
