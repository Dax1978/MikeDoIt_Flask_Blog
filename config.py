import os


BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# os.path.abspath(__name__)
# D:\Biblio\prog\python\Flask\Python Flask Tutorial - Blog project\flask_blog\app\config.py

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Для WINDOWS: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application