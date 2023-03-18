import secrets
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, HttpUrl

load_dotenv()  # take environment variables from .env.


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    DATABASE_DRIVER = "postgresql+psycopg2"

    PROJECT_NAME: str = "Base FastAPI"
    SENTRY_DSN: Optional[HttpUrl] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/server/core/templates/html/email"
    EMAILS_ENABLED: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"
