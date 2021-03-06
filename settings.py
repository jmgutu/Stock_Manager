import os

SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'flaskuser'
DB_PASSWORD = 'dbpw' # not required for cloud9
BLOG_DATABASE_NAME = 'stock_mng'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
print DB_URI
BASE_FOLDER = '/mnt/c/Programming/Stock_Manager/'
UPLOADED_IMAGES_DEST = BASE_FOLDER + 'static/images'
UPLOADED_IMAGES_URL = '/static/images/'
UPLOADS_DEFAULT_DEST = BASE_FOLDER + 'static/uploads/'
GENERATED_DOWNLOADS_FOLDER = BASE_FOLDER + 'generated/'
SQLALCHEMY_TRACK_MODIFICATIONS = False