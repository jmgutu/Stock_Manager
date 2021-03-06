from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
migrate = Migrate(app, db)

# markdown
md = Markdown(app, extensions=['fenced_code', 'tables'])

# images
uploaded_tables = UploadSet('tables', extensions=('xlsx'))
configure_uploads(app, (uploaded_tables))

from author import views
from part_mng import views
from categories import views
from package_mng import views
from assembly_mng import views
from lms_application import views
from xls_import_export import views