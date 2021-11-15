from src.xpto.common.config.common_settings import CommonSettings


class ApiSettings(CommonSettings):

    api_key: str = "api_key"
    orders_api: str
    invoices_api: str

    class Config:
        env_file = 'settings/api-dev.env'
        fields = {
            'api_key': {
                'env': 'api_key'
            },
            'orders_api': {
                'env': 'orders_api'
            },
            'invoices_api': {
                'env': 'invoices_api'
            },

        }
