import falcon

from .helpers import generate_formdata

# hooks to be executed on every request before reaching to the endpoint
app = falcon.API(before=[generate_formdata])


from .views import *