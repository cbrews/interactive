# Gloabl Config
DEBUG = True
PORT = 8080

# SQLALCHEMY Configs
SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/interactive"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

# Cryptography
SECRET_KEY = "loafer"
RANDOM_GENERATOR_LENGTH = 256
CRYPTO_HARD_SALT = "nosesarered"
