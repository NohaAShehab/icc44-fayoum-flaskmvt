

# connect to db --> dev --> sqlite

class Config:
    # any common config  --> will be added here
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class ProductionConfig(Config):
    # class variables
    DEBUG = False
    # will be modified to postgres
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


# prd ---> postgres

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}