from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    region: str = "eu-west-2"
    llm_model_env_var: str = "ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0"
    temperature: float = 0.3
    top_p: float = 0.1
    max_tokens: int = 2048
    annual_return_rate: float = 0.07
    inflation_rate: float = 0.07
    retirement_age: int = 60
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()