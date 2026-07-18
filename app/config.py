import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/voiceagent"
)

# Application
APP_NAME = os.getenv("APP_NAME", "Voice Agent Backend")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")