#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="./backups"

mkdir -p "$BACKUP_DIR"

docker exec postgres-db pg_dump -U postgres voiceagent > "$BACKUP_DIR/voiceagent_$TIMESTAMP.sql"

echo "Backup created: $BACKUP_DIR/voiceagent_$TIMESTAMP.sql"
