#!/bin/bash
docker compose exec -T project_template poetry run mypy .
