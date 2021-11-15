from src.xpto.common.config.common_settings import CommonSettings


class ApiSettings(CommonSettings):

    api_key: str

    class Config:
        env_file = 'settings/api-dev.env'
        fields = {
            'api_key': {
                'env': 'api_key'
            }
        }
