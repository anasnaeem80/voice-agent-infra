#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage:"
    echo "./restore.sh backups/file.sql"
    exit 1
fi

cat "$1" | docker exec -i postgres-db psql -U postgres voiceagent

echo "Restore completed."
