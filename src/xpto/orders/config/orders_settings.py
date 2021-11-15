from src.xpto.common.config.common_settings import CommonSettings


class OrdersSettings(CommonSettings):
    mongodb_conn_string: str

    class Config:
        env_file = 'settings/orders-dev.env'
        fields = {
            'mongodb_conn_string': {
                'env': 'mongodb_conn_string'
            }
        }
