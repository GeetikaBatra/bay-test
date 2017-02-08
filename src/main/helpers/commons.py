from falcon.util.uri import parse_query_string
from werkzeug.http import parse_options_header
from werkzeug.formparser import parse_form_data
from cStringIO import StringIO
import json


def generate_formdata(req, resp, params):
    """sets prarams['form'] to pass to every endpoint.
    """
    print "here"
    form = dict()
    files = dict()
    if req.method == 'GET':
        di = parse_query_string(req.query_string)
        form = dict(di)
        params['form'], params['files'] = dict(form), dict(files)
    else:
        if 'json' in req.get_header('content-type', None):
            form = json.load(req.stream)
            params['form'], params['files'] = dict(form), dict(files)
        else:
            mimetype, options = parse_options_header(req.get_header('content-type'))
            print mimetype
            data = req.stream.read()
            #print data
            environ = {'wsgi.input': StringIO(data),
                       'CONTENT_LENGTH': str(len(data)),
                       'CONTENT_TYPE': req.get_header('content-type'),
                       'REQUEST_METHOD': 'POST'}
            stream, tempform, tempfiles = parse_form_data(environ)
            print "tempform",tempform
            print "stream",stream
            print "tempfiles", tempfiles
            for item in tempform:
                form[item] = tempform[item]
            di = parse_query_string(req.query_string)
            for item in di:
                form[item] = di[item]
            for item in tempfiles:
                files[item] = tempfiles[item]
            params['form'], params['files'] = dict(form), dict(files)
            print "test"
    return True


class MyEncoder(json.JSONEncoder):
    """
    This functions encodes objects and return json
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)