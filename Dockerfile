FROM python:3.12-slim

# Install uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Copy workspace definition and shared package first (for caching)
COPY pyproject.toml ./
COPY shared/ shared/

# Install dashboard dependencies
COPY dashboard/pyproject.toml dashboard/pyproject.toml
RUN uv pip install --system -r dashboard/pyproject.toml ./shared/

# Install incoming dependencies (most deps already cached from dashboard)
COPY incoming/pyproject.toml incoming/pyproject.toml
RUN uv pip install --system -r incoming/pyproject.toml

# Copy the rest of the project
COPY . .
