import falcon
import json
from ..helpers import MyEncoder

class Test:
    """
       This is an endpoint for uploading file
    """
    def on_get(self, req, resp, form={}, files={}):
        resp_dict = {"success": True, "summary": "Testing \
        files", "data": []}
        resp_dict["data"]=[form]
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        print resp_dict
        #resp.body = json.dumps(resp_dict, cls=MyEncoder)

    def on_post(self, req, resp, form={}, files={}):
        resp_dict = {"success": True, "summary": "Testing \
        files", "data": []}
        resp_dict["data"]=[form]
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        print resp_dict
        #resp.body = json.dumps(resp_dict, cls=MyEncoder)