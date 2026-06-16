# GitHub Runners Docker Optimization Guide

This repository demonstrates best practices for speeding up GitHub Actions pipelines, with a strong focus on Docker, BuildKit, pre-built base images, and docker-compose integration tests.

## Key Optimizations

### 1. Pre-build Toolchain/Base Images
See `.github/workflows/build-base.yml`

### 2. Use BuildKit + docker buildx bake for efficient builds

### 3. Integration Tests with docker-compose
See `.github/workflows/integration.yml` for a full example using Kafka + Lambda-style producer.

## Broader Tips
- Larger runners
- Smart caching with actions/cache
- Parallel jobs
- Shallow clones, etc.

For details, read the full guide below.


## Integration Example Details

The `integration.yml` workflow:
- Uses `docker/bake-action` to build services defined in `docker-compose.yml` with full BuildKit caching.
- Starts Kafka + Zookeeper + a simple Python producer service (simulating a Lambda writing to a topic).
- The producer sends test messages to a Kafka topic and exits.

This pattern ensures fast, repeatable integration tests.

## Files Included
- `Dockerfile.base`
- `Dockerfile.producer`
- `docker-compose.yml`
- `producer.py`
- `requirements.txt`
- Workflows for base build and integration.

Clone this repo and adapt to your stack!