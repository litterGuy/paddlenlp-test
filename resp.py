from json import dumps

from flask import Response


class ErrorResponse(Response):
    def __init__(self, err_code, err_msg=''):
        result = dumps(dict(code=err_code, msg=err_msg))
        Response.__init__(self, result, mimetype='application/json')


class JSONResponse(Response):
    def __init__(self, data, msg=''):
        result = dumps(dict(data=data, code=0, msg=msg))
        Response.__init__(self, result, mimetype='application/json')
