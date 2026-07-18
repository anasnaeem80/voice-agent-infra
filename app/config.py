import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/voiceagent"
)

APP_NAME = "Voice Agent Backend"
APP_VERSION = "1.0.0"
