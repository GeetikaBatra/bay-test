from main import app
from .test import Test


test = Test()
app.add_route('/api/v1/test', test)
