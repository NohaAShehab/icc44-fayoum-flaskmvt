

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
    #postgres
    """
        db -> flask_fayoum
        user -> fayoum
        password -> iti 
        'postgresql://username:password@host:port/database_name'
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://fayoum:iti@localhost:5432/flask_fayoum'


# prd ---> postgres

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}