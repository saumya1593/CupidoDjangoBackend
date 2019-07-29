
# Create your models here.
from mongoengine import fields, Document, connect
from mongoengine.errors import OperationError

try:
    connection = connect(
        host='mongodb://e_user:password1@ds249017.mlab.com:49017/employee'
    )
    # db = connection['db_name']
    print(connection)
except OperationError:
    print("Error")

class employee_details(Document):
    name = fields.StringField(required=True)
    contact = fields.IntField(required=True)

    def employee_details(self):
        val = employee_details.objects.all()
        print(val)
        return employee_details.objects.all()