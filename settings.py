from starlette.config import Config

config = Config()

DEBUG = config("DEBUG", cast=bool, default=False)
