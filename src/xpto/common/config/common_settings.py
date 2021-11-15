from pydantic import BaseSettings, Field


class CommonSettings(BaseSettings):
    environment: str = Field(default='homolog')
    http_port: int

    class Config:
        env_file_encoding = 'utf-8'
        fields = {
            'environment': {
                'env': 'environment'
            },
            'http_port': {
                'env': 'http_port'
            }
        }
