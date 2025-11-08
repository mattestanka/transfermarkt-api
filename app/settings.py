from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # API rate limiting (FastAPI endpoint rate limiting)
    RATE_LIMITING_ENABLE: bool = False
    RATE_LIMITING_FREQUENCY: str = "2/3seconds"

    # HTTP request settings (for scraping Transfermarkt)
    REQUEST_TIMEOUT: int = 10  # seconds
    REQUEST_RATE_LIMIT: float = 0.5  # seconds between requests to avoid overloading Transfermarkt
    REQUEST_MAX_RETRIES: int = 2  # max retries for failed requests


settings = Settings()
