
from flask import  Blueprint

# define blueprint for this app >?
# apply this on any route == url uses this blueprint
student_blueprint = Blueprint('students', __name__, url_prefix='/students')

from app.students import  views